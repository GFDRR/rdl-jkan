---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/floodwater-depth-in-saint-louis-and-matam-regions-senegal-as-of-23-october-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floodwater-depth-in-saint-louis-and-matam-regions-senegal-as-of-23-october-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/floodwater-depth-in-saint-louis-and-matam-regions-senegal-as-of-23-october-2024
dataset_id: rdls_hzd-sen_unosat_floodwaterdepthsaintlouis_20241025
description: 'UNOSAT code: FL20241022SEN This map illustrates floodwater depth in
  in Saint-Louis and Matam Regions, Senegal observed from VIIRS flood depth data as
  of 23 October 2024. Important note: This map is prepared with a 30-m VIIRS satellite-derived
  Floodwater Depth product. It has been downscaled with software that uses VIIRS daily
  composite flood products at 375-m resolution as a basis. Products are under development
  and processed in near real-time at the Cooperative Institute for Meteorological
  Satellite Studies (CIMSS). This is a preliminary analysis intended to be used for
  guidance purposes and has yet to be validated with ground truth data. Please send
  field observations to United Nations Satellite Centre (UNOSAT).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/floodwater-depth-in-saint-louis-and-matam-regions-senegal-as-of-23-october-2024]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Floodwater depth data derived from VIIRS daily composite flood products
    at 375-m resolution, processed in near real-time at the Cooperative Institute
    for Meteorological Satellite Studies (CIMSS) and downscaled to 30-m resolution
    using specialized software. Satellite imagery was analyzed by UNOSAT analysts
    comparing multiple images to detect flood extent and depth changes in response
    to October 2024 flooding events in Senegal.
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
- href: https://data.humdata.org/dataset/floodwater-depth-in-saint-louis-and-matam-regions-senegal-as-of-23-october-2024
  rel: source
loss:
  losses: []
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
  description: Floodwater Depth in Saint-Louis and Matam Regions, Senegal as of 23
    October 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4008/FL20241022SEN_gdb.zip
  format: Geodatabase
  id: resource_25a366e6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241022SEN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Floodwater Depth in Saint-Louis and Matam Regions, Senegal as of 23
    October 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4008/FL20241022SEN_SHP.zip
  format: null
  id: resource_8a5bfd5a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241022SEN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sen_unosat_floodwaterdepthsaintlouis_20241025
spatial:
  bbox: null
  centroid: null
  countries:
  - SEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-10-25'
temporal_resolution: null
title: Floodwater Depth in Saint-Louis and Matam Regions, Senegal as of 23 October
  2024
version: null
vulnerability: null
---
