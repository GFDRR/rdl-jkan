---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-red-sea-district-as-of-15-august-2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-red-sea-district-as-of-15-august-2019
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-red-sea-district-as-of-15-august-2019
dataset_id: rdls_hzd-sdn_unosat_detectedwatersredseadistr_20190819
description: 'UNOSAT code: FL20190815SDN This map illustrates satellite-detected surface
  water in the eastern part of the Red Sea district in Sudan as observed from Sentinel-2
  image acquired on 15 August 2019. Within the analysed area of 1,500km2, 232 km2
  of lands appear to be flooded as of 15 August 2019. This is a preliminary analysis
  and has not yet validated in the field. Please send your ground feedback to UNITAR-UNOSAT.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-in-red-sea-district-as-of-15-august-2019]'
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
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed Sentinel-2 satellite imagery acquired on
    15 August 2019 over the Red Sea District, Sudan, using visual interpretation and
    multi-temporal image comparison to detect surface water extent changes. The analysis
    identified 232 km2 of flooded area within a 1,500 km2 study zone and produced
    vector geodatabase and shapefile outputs with area measurements in hectares and
    square meters.
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-in-red-sea-district-as-of-15-august-2019
  rel: source
loss: null
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
  description: Sudan - Satellite detected waters in Red Sea District as of 15 August
    2019 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20190815SDN/FL20190815SDN_gdb.zip
  format: Geodatabase
  id: resource_c775d82e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190815SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sudan - Satellite detected waters in Red Sea District as of 15 August
    2019 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20190815SDN/FL20190815SDN_SHP.zip
  format: null
  id: resource_4a1f0957
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190815SDN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_unosat_detectedwatersredseadistr_20190819
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-08-19'
temporal_resolution: null
title: Sudan - Satellite detected waters in Red Sea District as of 15 August 2019
version: null
vulnerability: null
---
