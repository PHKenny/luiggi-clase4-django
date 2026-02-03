CREATE OR REPLACE FUNCTION auth_user_t0001_set_api_token() RETURNS TRIGGER AS $$
DECLARE
  new_token TEXT;
BEGIN
  new_token := encode(gen_random_bytes(64), 'hex'); -- 128 characters

  LOOP
    BEGIN
      UPDATE auth_user SET api_token = new_token WHERE id = NEW.id;
      RETURN NEW;
    EXCEPTION WHEN unique_violation THEN
      -- If there's a unique violation, generate a new token and try again
      new_token := encode(gen_random_bytes(64), 'hex');
    END;
  END LOOP;
END $$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS t0001_set_api_token_create ON auth_user;
CREATE TRIGGER t0001_set_api_token_create AFTER INSERT ON auth_user
FOR EACH ROW EXECUTE FUNCTION auth_user_t0001_set_api_token();

DROP TRIGGER IF EXISTS t0001_set_api_token_renew ON auth_user;
CREATE TRIGGER t0001_set_api_token_renew AFTER UPDATE OF encrypted_password ON auth_user
FOR EACH ROW EXECUTE FUNCTION auth_user_t0001_set_api_token();
