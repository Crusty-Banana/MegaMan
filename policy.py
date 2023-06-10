frame_count_shooting = 0
frame_count_jumping = 0
def default_policy():
    #[shoot, dunno, dunno, up?, down?, left, right, jump]
    default_policy = [0, 0, 0, 0, 0, 0, 0, 1, 0]
    global frame_count_shooting, frame_count_jumping
    frame_count_shooting += 1
    if (frame_count_shooting == 10):
        frame_count_shooting = 0
        default_policy[0] = 1

    frame_count_jumping += 1
    if (frame_count_jumping > 30):
        default_policy[-1] = 1
    if (frame_count_jumping == 60):
        frame_count_jumping = 0

    return default_policy