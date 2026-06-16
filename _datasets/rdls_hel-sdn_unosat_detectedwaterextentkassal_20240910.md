---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-in-kassala-and-river-nile-states-sudan-as-of-3-and-5-september-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-in-kassala-and-river-nile-states-sudan-as-of-3-and-5-september-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-kassala-and-river-nile-states-sudan-as-of-3-and-5-september-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-kassala-and-river-nile-states-sudan-as-of-3-and-5-september-2024
dataset_id: rdls_hel-sdn_unosat_detectedwaterextentkassal_20240910
description: "UNOSAT code: FL20240826SDN, GDACS ID: 1102854 This map illustrates satellite-detected\
  \ water extents in Kassala and River Nile States, Sudan as observed from Sentinel-2\
  \ image acquired on 3 and 5 September 2024. Within the analysed area of about 100,000\
  \ km\xB2, a total of about 2,500 km\xB2 of land appears to be affected by floodwaters.\
  \ Based on Worldpop population data and the flood extent, approximately 39,000 people\
  \ are potentially exposed or living close to flooded areas. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/water-extent-in-kassala-and-river-nile-states-sudan-as-of-3-and-5-september-2024]"
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
    description: Population potentially exposed or living close to flooded areas derived
      from WorldPop data
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
  description: "UNOSAT analysts processed Sentinel-2 satellite imagery from 3 and\
    \ 5 September 2024 to detect water extent changes in Kassala and River Nile States\
    \ through visual interpretation and multi-temporal image comparison. Detected\
    \ flood extent (approximately 2,500 km\xB2) was overlaid with WorldPop population\
    \ data to estimate approximately 39,000 people potentially exposed to floodwaters.\
    \ This preliminary post-event analysis provides empirical hazard and exposure\
    \ data for flood impact assessment."
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
- href: https://data.humdata.org/dataset/water-extent-in-kassala-and-river-nile-states-sudan-as-of-3-and-5-september-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by fluvial flooding based on satellite-detected
      water extent and population overlay
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
  description: Satellite detected water extent in Kassala and River Nile States, Sudan
    as of 3 and 5 September 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3959/FL20240826SDN_gdb.zip
  format: Geodatabase
  id: resource_34ddd92b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240826SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Kassala and River Nile States, Sudan
    as of 3 and 5 September 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3959/FL20240826SDN_SHP.zip
  format: null
  id: resource_a66d7abf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240826SDN_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Kassala and River Nile States, Sudan
    as of 3 and 5 September 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3959/UNOSAT_FL20240826SDN_PopulationExposed_Khartoum.xlsx
  format: null
  id: resource_a184b68b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_FL20240826SDN_PopulationExposed_Khartoum.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-sdn_unosat_detectedwaterextentkassal_20240910
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
  start: '2024-09-10'
temporal_resolution: null
title: Satellite detected water extent in Kassala and River Nile States, Sudan as
  of 3 and 5 September 2024
version: null
vulnerability: null
---
