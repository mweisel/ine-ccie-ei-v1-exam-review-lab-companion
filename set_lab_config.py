from nornir import InitNornir
from nornir_scrapli.tasks import cfg_load_config, cfg_commit_config
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file


def apply_config(task):
    host_vars = task.run(
        task=load_yaml,
        file=f"inventory/host_vars/{task.host}.yaml",
    )
    task.host["facts"] = host_vars.result
    config_template = task.run(
        task=template_file,
        template="base.j2",
        path=f"templates/{task.host['type']}/",
    )
    config = config_template.result
    task.run(
        task=cfg_load_config,
        config=config,
        replace=True,
    )
    task.run(
        task=cfg_commit_config,
        source="running",
    )


def main():
    nr = InitNornir(config_file="config.yaml")
    results = nr.run(task=apply_config)
    print_result(results)


if __name__ == "__main__":
    main()
