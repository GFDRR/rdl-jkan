---
attributions:
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/water-extents-between-16-and-20-august-2024-over-far-north-region-cameroon
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-16-and-20-august-2024-over-far-north-region-cameroon
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-16-and-20-august-2024-over-far-north-region-cameroon
dataset_id: rdls_hel-cmr_unosat_detectedwaterextentsbetwe_20240822
description: "UNOSAT code: FL20240821CMR This map illustrates cumulative satellite-detected\
  \ water extent in Farth-North Region, Cameroon between 16 to 20 August 2024. Within\
  \ the cloud free analysed areas of about 33,000 km\xB2, a total of about 4,100 km\xB2\
  \ of lands appear to be affected with flood waters. Water extent appears to have\
  \ increased of about 2,500 km\xB2 since the period between 07 to 11 August 2024.\
  \ Based on Worldpop population data and the maximum flood water extent, ~350,000\
  \ people in Far-North Region are potentially exposed or living close to flooded\
  \ areas, amongst which ~130,000 people in Mayo-Kani Department and ~120,000 people\
  \ in Logone-et-Chari Department. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-between-16-and-20-august-2024-over-far-north-region-cameroon]"
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
    description: Population potentially exposed or living close to flooded areas in
      Far-North Region
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
  description: "Satellite imagery from multiple sensors acquired 16-20 August 2024\
    \ was analyzed by UNOSAT to detect cumulative water extent through multi-temporal\
    \ image comparison. Detected water areas (~4,100 km\xB2) were intersected with\
    \ Worldpop population data to estimate ~350,000 people potentially exposed to\
    \ flooding in Far-North Region, Cameroon."
  sources:
  - id: source_1
    license: null
    name: Worldpop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-between-16-and-20-august-2024-over-far-north-region-cameroon
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by or exposed to flood waters in Far-North Region,
      August 2024
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
  description: Satellite detected water extents between 16 and 20 August 2024 over
    Far-North Region, Cameroon (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3926/FL20240821CMR_gdb.zip
  format: Geodatabase
  id: resource_03015c6b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240821CMR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 16 and 20 August 2024 over
    Far-North Region, Cameroon (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3926/FL20240821CMR_SHP.zip
  format: null
  id: resource_de09d122
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240821CMR_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 16 and 20 August 2024 over
    Far-North Region, Cameroon (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3926/UNOSAT_Population_Exposure_FL20240821CMR_16Aug_20Aug2024_CMR.xlsx
  format: null
  id: resource_1c7f837e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20240821CMR_16Aug_20Aug2024_CMR.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cmr_unosat_detectedwaterextentsbetwe_20240822
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-22'
temporal_resolution: null
title: Satellite detected water extents between 16 and 20 August 2024 over Far-North
  Region, Cameroon
version: null
vulnerability: null
---
