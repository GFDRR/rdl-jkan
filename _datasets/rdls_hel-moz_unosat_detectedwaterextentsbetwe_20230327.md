---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-21-and-25-march-2023-over-mozambique
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-21-and-25-march-2023-over-mozambique
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-21-and-25-march-2023-over-mozambique
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-21-and-25-march-2023-over-mozambique
dataset_id: rdls_hel-moz_unosat_detectedwaterextentsbetwe_20230327
description: "UNOSAT code TC20230221MOZ, GDACS Id: 1000961 This map illustrates cumulative\
  \ satellite-detected water using VIIRS in Mozambique between 21 to 25 March 2023.\
  \ Within the cloud free analyzed areas of about 620,000 km\xB2, a total of about\
  \ 18,300 km\xB2 of lands appear to be affected with flood waters. Water extent appears\
  \ to have decreased of about 2,700 km2 since the 15-19 March 2023. Based on Worldpop\
  \ population data and the maximal flood water extent, ~1,300,000 people are potentially\
  \ exposed or living close to flooded areas mainly located in Zambezia province with\
  \ ~480,000 people, Nampula province with ~210,000 people and Sofala province with\
  \ ~ 210,000 people. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-21-and-25-march-2023-over-mozambique]"
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed VIIRS satellite imagery from 21-25 March\
    \ 2023 to detect cumulative water extents across cloud-free areas of Mozambique.\
    \ Detected flood water polygons (18,300 km\xB2 total) were intersected with WorldPop\
    \ gridded population data to estimate ~1.3 million people potentially exposed\
    \ to flooding, primarily in Zambezia province. This post-event empirical dataset\
    \ provides observed hazard extent and derived exposure metrics for the cyclone-triggered\
    \ flood event."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-21-and-25-march-2023-over-mozambique
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood water extent detected via satellite
      imagery
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
  description: Satellite detected water extents between 21 and 25 March 2023 over
    Mozambique (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3545/TC20230221MOZ.gdb.zip
  format: Geodatabase
  id: resource_99775d18
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 21 and 25 March 2023 over
    Mozambique (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3545/TC20230221MOZ_shp.zip
  format: null
  id: resource_d29b4db8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MOZ_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 21 and 25 March 2023 over
    Mozambique (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3545/UNOSAT_Population_Exposure_TC20230221MOZ_21Mar_25Mar2023_Mozambique.xlsx
  format: null
  id: resource_75284df9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_TC20230221MOZ_21Mar_25Mar2023_Mozambique.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-moz_unosat_detectedwaterextentsbetwe_20230327
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-27'
temporal_resolution: null
title: Satellite detected water extents between 21 and 25 March 2023 over Mozambique
version: null
vulnerability: null
---
