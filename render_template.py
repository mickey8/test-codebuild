import os
from jinja2 import Environment, FileSystemLoader


def render_template(template_name, **kwargs):
    env = Environment(loader=FileSystemLoader(os.path.join(os.environ['CODEBUILD_SRC_DIR'], 'template')))
    template = env.get_template(template_name)
    with open(template_name[:-3], 'w') as f:
        f.write(template.render(**kwargs))


if __name__ == '__main__':
    render_template(
        'sonarqube-vars.yml.j2',
        sonarqube_version=os.environ['sonarqube_version']
    )
