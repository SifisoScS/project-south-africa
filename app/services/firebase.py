import os
try:
    import firebase_admin
    from firebase_admin import credentials, messaging
except Exception:
    firebase_admin = None

def init_app(app):
    cred_path = app.config.get('FIREBASE_CREDENTIALS')
    if not cred_path:
        app.logger.info('No Firebase credentials provided; skipping init.')
        return None
    if firebase_admin is None:
        app.logger.warning('firebase_admin not installed; cannot init Firebase.')
        return None
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    app.logger.info('Firebase initialized.')
    return firebase_admin
