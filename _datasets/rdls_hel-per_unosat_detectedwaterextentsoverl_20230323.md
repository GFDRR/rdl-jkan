---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-22-march-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-22-march-2023
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-22-march-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-22-march-2023
dataset_id: rdls_hel-per_unosat_detectedwaterextentsoverl_20230323
description: "UNOSAT code EQ20230321PER, GDACS Id: 1365556 This map illustrates satellite-detected\
  \ water using Sentinel-2 acquired on 22 March 2023, 10:36 local time over Lambayeque\
  \ and Piura Provinces, Peru. Within the cloud free analyzed areas of about 16,000\
  \ km\xB2, a total of about 1,000 km\xB2 of lands appear to be affected with flood\
  \ waters. Based on Worldpop population data and flood water extent, ~13,500 people\
  \ in Lambayeque district are potentially exposed or living close to flooded areas\
  \ and ~6,300 people in Lambayeque district. This is a preliminary analysis and has\
  \ not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-22-march-2023]"
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
      Lambayeque and Piura districts
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts compared Sentinel-2 satellite imagery acquired on\
    \ 22 March 2023 with reference imagery to detect changes and map water extents\
    \ across 16,000 km\xB2 of cloud-free areas in Lambayeque and Piura Provinces.\
    \ Population exposure was estimated by intersecting the ~1,000 km\xB2 flood water\
    \ extent with WorldPop gridded population data to quantify potentially affected\
    \ populations in each district."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-22-march-2023
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood waters based on satellite-detected inundation
      extent and WorldPop data
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
  description: Satellite detected water extents over Lambayeque and Piura Province
    Provinces, Peru as of 22 March 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3542/EQ20230321PER_gdb.zip
  format: Geodatabase
  id: resource_079c1935
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230321PER_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents over Lambayeque and Piura Province
    Provinces, Peru as of 22 March 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3542/EQ20230321PER_SHP.zip
  format: null
  id: resource_004a41b3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230321PER_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents over Lambayeque and Piura Province
    Provinces, Peru as of 22 March 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3542/Satellite%20detected%20water%20%20extents%20over%20Peru%20as%20of%2022%20March%202023.csv
  format: null
  id: resource_769a93bd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Satellite detected water extents over Peru as of 22 March 2023.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-per_unosat_detectedwaterextentsoverl_20230323
spatial:
  bbox: null
  centroid: null
  countries:
  - PER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-23'
temporal_resolution: null
title: Satellite detected water extents over Lambayeque and Piura Province Provinces,
  Peru as of 22 March 2023
version: null
vulnerability: null
---
