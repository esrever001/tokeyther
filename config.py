project_name = "tokeyther"

plugins = [
    "oz.core",
    project_name,
]

app_options = dict(
    port = 8000,
    debug = True,
    static_path = "static",
    template_path = "templates",
    xsrf_cookies = False,
    gzip = False
)
