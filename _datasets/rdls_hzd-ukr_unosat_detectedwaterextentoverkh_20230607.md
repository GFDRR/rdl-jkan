---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-khersonska-oblast-ukraine-as-of-06-june-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-khersonska-oblast-ukraine-as-of-06-june-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-over-khersonska-oblast-ukraine-as-of-06-june-2023
dataset_id: rdls_hzd-ukr_unosat_detectedwaterextentoverkh_20230607
description: "UNOSAT code FL20230606UKR This map illustrates satellite-detected surface\
  \ waters over Khersonska Oblast, Ukraine observed from a Sentinel-3 image acquired\
  \ on 6 June 2023 at 08:30 UTC; and a Sentinel-2 image acquired on 3 & 5 June 2023.\
  \ Within the analysed area of 19,000 km\xB2, about 120 km\xB2 of land appear to\
  \ be flooded. This is a preliminary analysis and has not yet been validated in the\
  \ field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-over-khersonska-oblast-ukraine-as-of-06-june-2023]"
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed Sentinel-3 imagery acquired on 6 June 2023
    and Sentinel-2 imagery from 3-5 June 2023 over Khersonska Oblast, comparing multi-temporal
    satellite images to detect notable changes in surface water extent and identify
    flooded land areas. The analysis produced vector geometries of detected water
    bodies with area measurements, representing observed flood extent at a single
    point in time without field validation.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-over-khersonska-oblast-ukraine-as-of-06-june-2023
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
  description: Satellite detected water extent over Khersonska Oblast, Ukraine as
    of 06 June 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3611/FL20230606UKR_gdb.zip
  format: Geodatabase
  id: resource_b4abe8db
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Khersonska Oblast, Ukraine as
    of 06 June 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3611/FL20230606UKR_SHP.zip
  format: null
  id: resource_6740a58b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ukr_unosat_detectedwaterextentoverkh_20230607
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-06-07'
temporal_resolution: null
title: Satellite detected water extent over Khersonska Oblast, Ukraine as of 06 June
  2023
version: null
vulnerability: null
---
