from daes.calcul_statique_cylinder import run_calcul_statique_for_cylinder, save_displacements_to_images


def main() -> None:
    displacements = run_calcul_statique_for_cylinder(1.0, 0.5, 9.81, 1000, 0.001)
    save_displacements_to_images(displacements)
