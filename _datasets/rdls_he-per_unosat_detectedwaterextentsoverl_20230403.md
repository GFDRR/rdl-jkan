---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-1-april-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-1-april-2023
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-1-april-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-1-april-2023
dataset_id: rdls_he-per_unosat_detectedwaterextentsoverl_20230403
description: "UNOSAT code FL20230321PER, GDACS Id: 1365556 This map illustrates satellite-detected\
  \ water using Sentinel-2 acquired on 1 April 2023, 10:36 local time over Lambayeque\
  \ and Piura Provinces, Peru. Within the cloud free analyzed areas of about 13,000\
  \ km\xB2, a total of about 1,000 km\xB2 of lands appear to be affected with flood\
  \ waters. Based on Worldpop population data and the flood water extent, ~13,000\
  \ people are potentially exposed or living close to flooded areas mainly located\
  \ in District of Piura with ~3,800 people, Piura District with ~3,800 people, Sechura\
  \ with ~3,800 people, and Lambayeque ~3,600 people This is a preliminary analysis\
  \ and has not yet been validated in the field. Please send ground feedback to the\
  \ United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-1-april-2023]"
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
    description: Population potentially exposed or living close to flooded areas,
      estimated at ~13,000 people based on WorldPop data
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
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed Sentinel-2 satellite imagery acquired on\
    \ 1 April 2023 over Lambayeque and Piura Provinces, Peru, comparing multi-temporal\
    \ images to detect notable changes in water extent. Detected flood water polygons\
    \ (~1,000 km\xB2 across ~13,000 km\xB2 analyzed area) were intersected with WorldPop\
    \ population grids to estimate exposure of ~13,000 people to flooded areas by\
    \ administrative district."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2
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
- href: https://data.humdata.org/dataset/water-extents-over-lambayeque-and-piura-province-provinces-peru-as-of-1-april-2023
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
  description: Satellite detected water extents over Lambayeque and Piura Province
    Provinces, Peru as of 1 April 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3555/FL20230321PER_gdb.zip
  format: Geodatabase
  id: resource_eeab8613
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230321PER_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents over Lambayeque and Piura Province
    Provinces, Peru as of 1 April 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3555/FL0230321PER_SHP.zip
  format: null
  id: resource_80606a54
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL0230321PER_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents over Lambayeque and Piura Province
    Provinces, Peru as of 1 April 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3555/Satellite%20detected%20water%20extents%20over%20Lambayeque%20and%20Piura%20Province%20Provinces%2C%20Peru%20%20as%20of%2003%20Apr%202023%20-%20Copy.csv
  format: null
  id: resource_f34c4d49
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Satellite detected water extents over Lambayeque and Piura Province Provinces,
    Peru as of 03 Apr 2023 - Copy.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-per_unosat_detectedwaterextentsoverl_20230403
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
  start: '2023-04-03'
temporal_resolution: null
title: Satellite detected water extents over Lambayeque and Piura Province Provinces,
  Peru as of 1 April 2023
version: null
vulnerability: null
---
