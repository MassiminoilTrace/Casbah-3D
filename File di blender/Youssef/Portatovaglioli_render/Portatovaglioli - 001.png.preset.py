import bpy
scene = bpy.context.scene

scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 50
scene.render.border_max_x = 1.0
scene.render.border_max_y = 1.0
scene.render.border_min_x = 0.0
scene.render.border_min_y = 0.0
scene.render.use_border = False
scene.render.use_crop_to_border = False
scene.gs_ray_depth = 2
scene.gs_shadow_depth = 2
scene.gs_threads = 1
scene.display_settings.display_device = 'sRGB'
scene.gs_gamma = 1.0
scene.gs_gamma_input = 1.0
scene.gs_tile_size = 32
scene.gs_tile_order = 'centre'
scene.gs_tex_optimization = 'optimized'
scene.gs_auto_threads = True
scene.gs_clay_render = False
scene.gs_clay_render_keep_transparency = False
scene.gs_clay_render_keep_normals = False
scene.gs_clay_oren_nayar = True
scene.gs_clay_sigma = 0.3
scene.gs_clay_col = (0.2160000056028366, 0.2160000056028366, 0.2160000056028366)
scene.gs_mask_render = False
scene.bg_transp = False
scene.bg_transp_refract = True
scene.adv_auto_shadow_bias_enabled = True
scene.adv_shadow_bias_value = 0.0005
scene.adv_auto_min_raydist_enabled = True
scene.adv_min_raydist_value = 0.0
scene.gs_premult = 'auto'
scene.gs_transp_shad = False
scene.gs_show_sam_pix = True
scene.gs_type_render = 'into_blender'
scene.gs_tex_optimization = 'optimized'
scene.intg_light_method = 'Direct Lighting'
scene.intg_use_caustics = False
scene.intg_photons = 500000
scene.intg_caustic_mix = 100
scene.intg_caustic_depth = 10
scene.intg_caustic_radius = 1.0
scene.intg_use_AO = False
scene.intg_AO_samples = 32
scene.intg_AO_distance = 1.0
scene.intg_AO_color = (0.8999999761581421, 0.8999999761581421, 0.8999999761581421)
scene.intg_photonmap_enable_caustics = True
scene.intg_photonmap_enable_diffuse = True
scene.intg_bounces = 4
scene.intg_diffuse_radius = 1.0
scene.intg_cPhotons = 500000
scene.intg_search = 100
scene.intg_final_gather = True
scene.intg_fg_bounces = 3
scene.intg_fg_samples = 16
scene.intg_show_map = False
scene.intg_caustic_method = 'None'
scene.intg_path_samples = 32
scene.intg_no_recursion = False
scene.intg_debug_type = 'dSdV'
scene.intg_show_perturbed_normals = False
scene.intg_pm_ire = False
scene.intg_pass_num = 1000
scene.intg_times = 1.0
scene.intg_photon_radius = 1.0
scene.AA_min_samples = 1
scene.AA_inc_samples = 1
scene.AA_passes = 1
scene.AA_threshold = 0.05
scene.AA_pixelwidth = 1.5
scene.AA_filter_type = 'gauss'
scene.yafaray.noise_control.resampled_floor = 0.0
scene.yafaray.noise_control.sample_multiplier_factor = 1.0
scene.yafaray.noise_control.light_sample_multiplier_factor = 1.0
scene.yafaray.noise_control.indirect_sample_multiplier_factor = 1.0
scene.yafaray.noise_control.detect_color_noise = False
scene.yafaray.noise_control.dark_threshold_factor = 0.0
scene.yafaray.noise_control.variance_edge_size = 10
scene.yafaray.noise_control.variance_pixels = 0
scene.yafaray.noise_control.clamp_samples = 0.0
scene.yafaray.noise_control.clamp_indirect = 0.0
scene.render.layers[0].use_pass_z = True
scene.render.layers[0].use_pass_vector = False
scene.render.layers[0].use_pass_normal = False
scene.render.layers[0].use_pass_uv = False
scene.render.layers[0].use_pass_color = False
scene.render.layers[0].use_pass_emit = False
scene.render.layers[0].use_pass_mist = False
scene.render.layers[0].use_pass_diffuse = False
scene.render.layers[0].use_pass_specular = False
scene.render.layers[0].use_pass_ambient_occlusion = False
scene.render.layers[0].use_pass_environment = False
scene.render.layers[0].use_pass_indirect = False
scene.render.layers[0].use_pass_shadow = False
scene.render.layers[0].use_pass_reflection = False
scene.render.layers[0].use_pass_refraction = False
scene.render.layers[0].use_pass_object_index = False
scene.render.layers[0].use_pass_material_index = False
scene.render.layers[0].use_pass_diffuse_direct = False
scene.render.layers[0].use_pass_diffuse_indirect = False
scene.render.layers[0].use_pass_diffuse_color = False
scene.render.layers[0].use_pass_glossy_direct = False
scene.render.layers[0].use_pass_glossy_indirect = False
scene.render.layers[0].use_pass_glossy_color = False
scene.render.layers[0].use_pass_transmission_direct = False
scene.render.layers[0].use_pass_transmission_indirect = False
scene.render.layers[0].use_pass_transmission_color = False
scene.render.layers[0].use_pass_subsurface_direct = False
scene.render.layers[0].use_pass_subsurface_indirect = False
scene.render.layers[0].use_pass_subsurface_color = False
scene.yafaray.passes.pass_enable = False
scene.yafaray.passes.pass_mask_obj_index = 0
scene.yafaray.passes.pass_mask_mat_index = 0
scene.yafaray.passes.pass_mask_invert = False
scene.yafaray.passes.pass_mask_only = False
scene.yafaray.passes.pass_Combined = 'disabled'
scene.yafaray.passes.pass_Depth = 'z-depth-norm'
scene.yafaray.passes.pass_Vector = 'obj-index-auto'
scene.yafaray.passes.pass_Normal = 'debug-normal-smooth'
scene.yafaray.passes.pass_UV = 'debug-uv'
scene.yafaray.passes.pass_Color = 'mat-index-auto'
scene.yafaray.passes.pass_Emit = 'emit'
scene.yafaray.passes.pass_Mist = 'mist'
scene.yafaray.passes.pass_Diffuse = 'diffuse'
scene.yafaray.passes.pass_Spec = 'adv-reflect'
scene.yafaray.passes.pass_AO = 'ao'
scene.yafaray.passes.pass_Env = 'env'
scene.yafaray.passes.pass_Indirect = 'indirect'
scene.yafaray.passes.pass_Shadow = 'shadow'
scene.yafaray.passes.pass_Reflect = 'reflect'
scene.yafaray.passes.pass_Refract = 'refract'
scene.yafaray.passes.pass_IndexOB = 'obj-index-norm'
scene.yafaray.passes.pass_IndexMA = 'mat-index-norm'
scene.yafaray.passes.pass_DiffDir = 'diffuse'
scene.yafaray.passes.pass_DiffInd = 'adv-diffuse-indirect'
scene.yafaray.passes.pass_DiffCol = 'adv-diffuse-color'
scene.yafaray.passes.pass_GlossDir = 'adv-glossy'
scene.yafaray.passes.pass_GlossInd = 'adv-glossy-indirect'
scene.yafaray.passes.pass_GlossCol = 'adv-glossy-color'
scene.yafaray.passes.pass_TransDir = 'adv-trans'
scene.yafaray.passes.pass_TransInd = 'adv-trans-indirect'
scene.yafaray.passes.pass_TransCol = 'adv-trans-color'
scene.yafaray.passes.pass_SubsurfaceDir = 'adv-subsurface'
scene.yafaray.passes.pass_SubsurfaceInd = 'adv-subsurface-indirect'
scene.yafaray.passes.pass_SubsurfaceCol = 'adv-subsurface-color'
