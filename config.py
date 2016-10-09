
env = dict(
	host = '0.0.0.0',
	port = 3000,
	user = 'root',
	password = 'root',
	db = 'EPANTRY',
)

SQLALCHEMY_DATABASE_URI = 'mysql://' + env('user') + env('password') + '@' + env('host') + ':' + env('port') + '/' + \
                          env('db')
