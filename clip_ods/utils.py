import numpy as np


def get_anchor_coords(image_w, image_h, count_w, count_h):
    step_w = image_w // count_w + 1
    step_h = image_h // count_h + 1

    w_coords = np.arange(0, image_w + step_w, step_w)
    h_coords = np.arange(0, image_h + step_h, step_h)

    coords = []
    for x1, x2 in zip(w_coords[:-1], w_coords[1:]):
        x1, x2 = min(x1, image_w), min(x2, image_w)
        for y1, y2 in zip(h_coords[:-1], h_coords[1:]):
            y1, y2 = min(y1, image_h), min(y2, image_h)
            coords.append((x1, y1, x2, y2))

            anchor_w = (x2 - x1) / 2
            anchor_h = (y2 - y1) / 2
            anchor_xc = (x2 + x1) // 2
            anchor_yc = (y2 + y1) // 2

            for coef_x, coef_y in [
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
                (1, 2), (2, 1),
                (2, 3), (3, 2),
                (2, 4), (4, 2),
                (3, 1), (1, 3),
                (5, 4), (4, 5),
                (4, 1), (1, 4),
                (5, 1), (1, 5),
                (5, 3), (3, 5),
                (6, 4), (4, 6),
                (5, 8), (8, 5),
                (10, 2), (2, 10),
                (10, 4), (4, 10),
                (10, 6), (6, 10),
                (10, 8), (8, 10),
            ]:
                anc_x1 = max(anchor_xc - (anchor_w * coef_x), 0)
                anc_x2 = min(anchor_xc + (anchor_w * coef_x), image_w)
                anc_y1 = max(anchor_yc - (anchor_h * coef_y), 0)
                anc_y2 = min(anchor_yc + (anchor_h * coef_y), image_h)
                coords.append((anc_x1, anc_y1, anc_x2, anc_y2))

    return coords
