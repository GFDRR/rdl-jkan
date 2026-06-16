---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-uribia-municipality-la-guajira-department-colombia-as-of-15-nov
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-uribia-municipality-la-guajira-department-colombia-as-of-15-nov
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-uribia-municipality-la-guajira-department-colombia-as-of-15-nov
dataset_id: rdls_hel-col_unosat_floodimpactassessmenturib_20241122
description: "UNOSAT code: FL20241112COL, GDACS ID: 1102988 This map illustrates satellite-detected\
  \ water extent in Uribia Municipality, La Guajira Department, Colombia as observed\
  \ from a Sentinel-2 satellite image acquired on 15 November 2024 at 10:17 Local\
  \ Time. Within the analysed area of about 220 km\xB2, a total of about 24 km\xB2\
  \ of lands appear to be affected with flood waters. UNOSAT identified 529 structures\
  \ that appear to be not affected by flood waters. This is a preliminary analysis\
  \ and has not yet been validated in the field. Please send ground feedback to the\
  \ United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-assessment-in-uribia-municipality-la-guajira-department-colombia-as-of-15-nov]"
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
    description: Building structures identified in the analysis area, with 529 structures
      assessed for flood exposure
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
      quantity_kind: count
      unit: count
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
  description: "Sentinel-2 satellite imagery acquired on 15 November 2024 was analyzed\
    \ by UNOSAT analysts through visual interpretation and multi-temporal comparison\
    \ to detect flood water extent and identify affected structures. The analysis\
    \ identified approximately 24 km\xB2 of inundated area within a 220 km\xB2 study\
    \ area in Uribia Municipality, with 529 structures assessed for flood impact.\
    \ This is a preliminary satellite-based assessment not yet validated through field\
    \ surveys."
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
- href: https://data.humdata.org/dataset/flood-impact-assessment-in-uribia-municipality-la-guajira-department-colombia-as-of-15-nov
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected structures affected by flood waters in Uribia
      Municipality as of 15 November 2024
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Flood impact assessment in Uribia Municipality, La Guajira Department,
    Colombia as of 15 November 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4038/FL20241112COL_gdb.zip
  format: Geodatabase
  id: resource_c5ec9eed
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241112COL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood impact assessment in Uribia Municipality, La Guajira Department,
    Colombia as of 15 November 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4038/FL20241112COL_SHP.zip
  format: null
  id: resource_bf8baae5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241112COL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-col_unosat_floodimpactassessmenturib_20241122
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-11-22'
temporal_resolution: null
title: Flood impact assessment in Uribia Municipality, La Guajira Department, Colombia
  as of 15 November 2024
version: null
vulnerability: null
---
