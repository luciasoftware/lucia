# Original code by Blastbay, created for the Blastbay gaming toolkit
# Ported to python by Carter Temm, with small modifications by Amerikranian
# Used with permition

import math


def position_sound_1d(handle, listener_x, source_x, pan_step, volume_step):
	position_sound_custom_1d(handle, listener_x, source_x, pan_step, volume_step, 0.0, 0.0)


def position_sound_custom_1d(
	handle, listener_x, source_x, pan_step, volume_step, start_pan, start_volume
):
	delta = 0
	final_pan = start_pan
	final_volume = start_volume
	# First, we calculate the delta between the listener and the source.
	if source_x < listener_x:
		delta = listener_x - source_x
		final_pan -= delta * pan_step
		final_volume -= delta * volume_step
	if source_x > listener_x:
		delta = source_x - listener_x
		final_pan += delta * pan_step
		final_volume -= delta * volume_step
	# Then we check if the calculated values are out of range, and fix them if that's the case.
	if final_pan < -100:
		final_pan = -100
	if final_pan > 100:
		final_pan = 100
	if final_volume < -100:
		final_volume = -100
	# Now we set the properties on the sound, provided that they are not already correct.
	if handle.pan != final_pan:
		handle.pan = final_pan
	if handle.volume != final_volume:
		handle.volume = final_volume


def position_sound_2d(
	handle,
	listener_x,
	listener_y,
	source_x,
	source_y,
	theta,
	pan_step,
	volume_step,
	behind_pitch_decrease,
	keep_pitch=False,
):
	position_sound_custom_2d(
		handle,
		listener_x,
		listener_y,
		source_x,
		source_y,
		theta,
		pan_step,
		volume_step,
		behind_pitch_decrease,
		0.0,
		0.0,
		100.0,
		keep_pitch,
	)


def position_sound_custom_2d(
	handle,
	listener_x,
	listener_y,
	source_x,
	source_y,
	theta,
	pan_step,
	volume_step,
	behind_pitch_decrease,
	start_pan,
	start_volume,
	start_pitch,
	keep_pitch,
):
	delta_x = 0
	delta_y = 0
	final_pan = start_pan
	final_volume = start_volume
	final_pitch = start_pitch
	rotational_source_x = source_x
	rotational_source_y = source_y
	# First, we calculate the x and y based on the theta the listener is facing.
	if theta > 0.0:
		rotational_source_x = (
			(math.cos(theta) * (source_x - listener_x))
			- (math.sin(theta) * (source_y - listener_y))
			+ listener_x
		)
		rotational_source_y = (
			(math.sin(theta) * (source_x - listener_x))
			+ (math.cos(theta) * (source_y - listener_y))
			+ listener_y
		)
		source_x = rotational_source_x
		source_y = rotational_source_y
	# Next, we calculate the delta between the listener and the source.
	if source_x < listener_x:
		delta_x = listener_x - source_x
		final_pan -= delta_x * pan_step
		final_volume -= delta_x * volume_step
	if source_x > listener_x:
		delta_x = source_x - listener_x
		final_pan += delta_x * pan_step
		final_volume -= delta_x * volume_step
	if source_y < listener_y:
		final_pitch -= abs(behind_pitch_decrease)
		delta_y = listener_y - source_y
		final_volume -= delta_y * volume_step
	if source_y > listener_y:
		delta_y = source_y - listener_y
		final_volume -= delta_y * volume_step
	# Then we check if the calculated values are out of range, and fix them if that's the case.
	if final_pan < -100:
		final_pan = -100
	if final_pan > 100:
		final_pan = 100
	if final_volume < -100:
		final_volume = -100
	if final_pitch < 0:
		final_pitch = 0
	# We don't check for the highest possible pitch as it is hard to determine.
	# Now we set the properties on the sound, provided that they are not already correct.
	if handle.pan != final_pan:
		handle.pan = final_pan
	if handle.volume != final_volume:
		handle.volume = final_volume
	if not keep_pitch:
		if handle.pitch != final_pitch:
			handle.pitch = final_pitch


def position_sound_3d(
	handle,
	listener_x,
	listener_y,
	listener_z,
	source_x,
	source_y,
	source_z,
	theta,
	pan_step,
	volume_step,
	behind_pitch_decrease,
	keep_pitch=False,
):
	position_sound_custom_3d(
		handle,
		listener_x,
		listener_y,
		listener_z,
		source_x,
		source_y,
		source_z,
		theta,
		pan_step,
		volume_step,
		behind_pitch_decrease,
		0.0,
		0.0,
		100.0,
		keep_pitch,
	)


def position_sound_custom_3d(
	handle,
	listener_x,
	listener_y,
	listener_z,
	source_x,
	source_y,
	source_z,
	theta,
	pan_step,
	volume_step,
	behind_pitch_decrease,
	start_pan,
	start_volume,
	start_pitch,
	keep_pitch,
):
	delta_x = 0
	delta_y = 0
	delta_z = 0
	final_pan = start_pan
	final_volume = start_volume
	final_pitch = start_pitch
	rotational_source_x = source_x
	rotational_source_y = source_y
	# First, we calculate the x and y based on the theta the listener is facing.
	if theta > 0.0:
		rotational_source_x = (
			(math.cos(theta) * (source_x - listener_x))
			- (math.sin(theta) * (source_y - listener_y))
			+ listener_x
		)
		rotational_source_y = (
			(math.sin(theta) * (source_x - listener_x))
			+ (math.cos(theta) * (source_y - listener_y))
			+ listener_y
		)
		source_x = rotational_source_x
		source_y = rotational_source_y
	# Next, we calculate the delta between the listener and the source.
	if source_x < listener_x:
		delta_x = listener_x - source_x
		final_pan -= delta_x * pan_step
		final_volume -= delta_x * volume_step
	if source_x > listener_x:
		delta_x = source_x - listener_x
		final_pan += delta_x * pan_step
		final_volume -= delta_x * volume_step
	if source_y < listener_y:
		final_pitch -= abs(behind_pitch_decrease)
		delta_y = listener_y - source_y
		final_volume -= delta_y * volume_step
	if source_y > listener_y:
		delta_y = source_y - listener_y
		final_volume -= delta_y * volume_step
	if source_z < listener_z:
		final_pitch -= abs(behind_pitch_decrease)
		delta_z = listener_z - source_z
		final_volume -= delta_z * volume_step
	if source_z > listener_z:
		delta_z = source_z - listener_z
		final_volume -= delta_z * volume_step
	# Then we check if the calculated values are out of range, and fix them if that's the case.
	if final_pan < -100:
		final_pan = -100
	if final_pan > 100:
		final_pan = 100
	if final_volume < -100:
		final_volume = -100
	if final_pitch < 0:
		final_pitch = 0
	# don't check for the highest possible pitch as it is hard to determine.
	# Now we set the properties on the sound, provided that they are not already correct.
	if handle.pan != final_pan:
		handle.pan = final_pan
	if handle.volume != final_volume:
		handle.volume = final_volume
	if not keep_pitch:
		if handle.pitch != final_pitch:
			handle.pitch = final_pitch
