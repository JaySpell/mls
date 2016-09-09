import config
import mech_it

def main(*args, **kwargs):
    
    config_info = {
            'l_url': config.l_url(),
            'q_url': config.get_q_url(),
            'cs_url': config.get_cs_url(),
            'user': config.get_user(),
            'password': config.get_password()
        }

    mech_it.get_mls_data(config_info)

if __init__ == '__main__':
    main()
