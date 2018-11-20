def process(request, **kwargs):
    app = 'ApiManager'
    fun = kwargs.pop('function', None)
    index = kwargs.pop('id', None)

    if fun is None:
        fun = 'login'
    try:
        app = __import__("%s.views" % app)
        view = getattr(app, 'views')
        fun = getattr(view, fun)

        # 执行view.py中的函数，并获取其返回值
        result = fun(request, index) if index else fun(request)
    except (ImportError, AttributeError):
        raise

    return result
