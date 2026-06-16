---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme
    url: https://data.humdata.org/dataset/wfp_ica_tza_2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_tza_2019
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp_ica_tza_2019
dataset_id: rdls_el-tza_wfp_unitedrepublicintegratedc_2019
description: 'The ICA is a process of consultations supported by mapped-out data that
  produces a strategic plan describing where different combinations of programme themes
  are appropriate to achieve goals of reducing food insecurity and climate related
  shock risk. The ICA combines multi-year food security trends with natural shock
  risk data to highlight sub-national areas where different programme strategies make
  sense. Food security trend maps shows areas where safety nets can address regular
  food insecurity, and others where shocks make recovery more important. Climate-related
  natural shock risk maps show where DRR, preparedness and early warning efforts can
  complement food-security objectives. Atop this core foundation, mapped data on subjects
  including nutrition, gender, livelihoods and resilience can enrich theme-level strategic
  planning in which all pieces work together. The full group of ICA partners discuss
  these analytical results to arrive at strategic programmatic directions.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/wfp_ica_tza_2019]'
details: null
exposure:
- asset_type:
    description: Long-term planning population and population density across livelihood
      zones
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Land cover and land use classification including agricultural areas
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Land degradation extent and land cover change assessment
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_3
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: ODbL-1.0/
lineage:
  description: The ICA combines multi-year food security trend analysis with natural
    shock hazard mapping (drought, flood, erosion, landslide) to produce sub-national
    strategic planning layers. Hazard data were inferred from climate and environmental
    indicators, integrated with population and livelihood zone data, and cross-referenced
    with food insecurity and malnutrition outcomes to identify areas where different
    programme interventions (safety nets vs. shock recovery) are appropriate.
  sources:
  - id: source_1
    license: null
    name: World Food Programme
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp_ica_tza_2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity prevalence and affected population from drought-related
      shocks
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural vulnerability and malnutrition outcomes linked to drought
      impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/82ef51980e1441b2abd7aa29794138a5/data
  format: null
  id: resource_9d642d3a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_CollectingTable
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/339459f32a144cb381c86febbaa65ebb/data
  format: PNG
  id: resource_fd258504
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_Categories_A4L_20191209
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/8eb3c76d49084f3faeec57c92d6905a8/data
  format: PNG
  id: resource_19de937b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_FoodInsecurity_A4L_20191209
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2bc7239625024f299f9e409e0380876c/data
  format: PNG
  id: resource_c2fe910a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_DroughtHazard_A4L_20191209
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c6cd546bfcae473892f7237577f3a07b/data
  format: PNG
  id: resource_022b4141
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_FloodHazard_A4L_20191209
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/c5040f12bd3940519081d603350a0e35/data
  format: PNG
  id: resource_219f3778
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_Erosion_OK_A4L_20191209
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4ead00ee7aa84b849d784a1f10073410/data
  format: PNG
  id: resource_f84f3a52
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_Erosion_A4L_20191212
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a286dfb194e44db195360851398f1abe/data
  format: PNG
  id: resource_742b586f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_LTPlanPop_A4L_20191209
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/79ea9a37e0864559a48b04ae97596bc2/data
  format: PNG
  id: resource_c1a591f8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_LandCoverChange_A4L_20191212
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/068bdedec3a342618ec9bef5e61ded9c/data
  format: PNG
  id: resource_a58c7956
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_Areas_A4L_20191209
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/a0605c5bd6c849b4ba5f7d58d3dfc241/data
  format: PNG
  id: resource_8052f2bb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_Areas_PopDensity_A4L_20191210
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/d27c442e32974eb1a4ece20ed671b96d/data
  format: PNG
  id: resource_5a3a317f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_NSHazard_A4L_20191209
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/dc530281bfba4d66ad200aa897a0dc35/data
  format: PNG
  id: resource_a3c6f00a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_Areas_LandDegradation_PopDens_A4L_20191213
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/2f54e5ca4c6c4ecca01b1940c856c709/data
  format: PNG
  id: resource_dff5c782
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_AdInsecPop_A4L_20191209
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/7205b787f6864e3786bc1fdbe43e3678/data
  format: PNG
  id: resource_f8149e7b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_Areas_Malnutrition_A4L_20191210
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/435539c550164c588ebae59a2195310d/data
  format: PNG
  id: resource_92b97aea
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_MostPredLHZ_A4L_20191210
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/4201cdbe07624e8384b95f8c773967f5/data
  format: PNG
  id: resource_281af4ba
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_PrevalenceStunting_A4L_20191210
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/fb4a8bcac92247cfbb0a9b68e2fb4d51/data
  format: PNG
  id: resource_293689c8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_LandslideHazard_A4L_20191209
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019
    (No abstract provided)'
  download_url: https://unwfp.maps.arcgis.com/sharing/rest/content/items/5557536ea2bf4b92a8d6090499a04593/data
  format: PNG
  id: resource_3e191daf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TZA_ICA_Areas_LandDegradation_A4L_20191211
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-tza_wfp_unitedrepublicintegratedc_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-12-31'
  start: '2019-01-01'
temporal_resolution: null
title: 'United Republic of Tanzania: Integrated Context Analysis (ICA), 2019'
version: null
vulnerability: null
---
