---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-ghat-city-ghat-governorate-south-province-libya-as-of-18-august-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-ghat-city-ghat-governorate-south-province-libya-as-of-18-august-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-ghat-city-ghat-governorate-south-province-libya-as-of-18-august-2024
dataset_id: rdls_hel-lby_unosat_detectedwaterextentghatci_20240821
description: "UNOSAT code: FL20240812LBY This map illustrates satellite-detected water\
  \ extent in Ghat City, Ghat Governorate, South Province, Libya as observed from\
  \ a WorldView-3 satellite image acquired on 18 August 2024 at 11:53 local time (09:53\
  \ UTC). Within analysed area of about 65km\xB2, a total of about 13 km\xB2 of land\
  \ appears to be affected by floodwaters. In Ghat City, approximately 5 km\xB2 (30%)\
  \ of the city is flooded, which includes around 0.5 km\xB2 of built-up area. Additionally,\
  \ about 13km of road is affected by the flooding This is a preliminary analysis\
  \ and has not yet been validated in the field. Please send ground feedback to the\
  \ United Nations Satellite Centre (UNOSAT). [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-ghat-city-ghat-governorate-south-province-libya-as-of-18-august-2024]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Built-up area in Ghat City affected by flood extent mapping
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Road network affected by floodwaters in the study area
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed WorldView-3 satellite imagery acquired on
    18 August 2024 over Ghat City, comparing pre- and post-flood images to delineate
    water extent and inundated areas. Satellite-detected flood polygons were vectorized
    with confidence levels and field validation flags to produce georeferenced water
    extent maps in shapefile and geodatabase formats.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-in-ghat-city-ghat-governorate-south-province-libya-as-of-18-august-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: "Direct flood inundation of built-up area in Ghat City (0.5 km\xB2\
      \ affected)"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct flood impact on road infrastructure (13 km affected)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Satellite detected water extent in Ghat City, Ghat Governorate, South
    Province, Libya as of 18 August 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3922/FL20240812LBY_gdb.zip
  format: Geodatabase
  id: resource_43392807
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240812LBY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Ghat City, Ghat Governorate, South
    Province, Libya as of 18 August 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3922/FL20240812LBY_SHP.zip
  format: null
  id: resource_a841b07c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240812LBY_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-lby_unosat_detectedwaterextentghatci_20240821
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-21'
temporal_resolution: null
title: Satellite detected water extent in Ghat City, Ghat Governorate, South Province,
  Libya as of 18 August 2024
version: null
vulnerability: null
---
