---
attributions:
- entity:
    affiliation: null
    email: null
    name: MODIS satellite sensor
    url: https://data.humdata.org/dataset/el-fasher-damage-assessment-overview
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: VIIRS satellite sensor
    url: https://data.humdata.org/dataset/el-fasher-damage-assessment-overview
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNOSAT satellite imagery analysis
    url: https://data.humdata.org/dataset/el-fasher-damage-assessment-overview
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/el-fasher-damage-assessment-overview
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/el-fasher-damage-assessment-overview
dataset_id: rdls_hl-sdn_unosat_elfasherdamageassessmento_20240814
description: 'UNOSAT code: CE20230415SDN This map illustrates damage to structures
  in the city of El Fasher, North Darfur, Republic of Sudan. The damage was investigated
  due to a significant occurrence of fire detections from May 9-20 2024. Fire detections
  are sourced from multiple US Government scientific satellites utilizing the MODIS
  and VIIRS sensors. While some fire detections may be non-violent in nature the large
  majority are firmly within areas of residential structures that show indications
  of burning in satellite imagery. Damaged areas are visible in satellite imagery
  from 11 November 2023 - 31 July 2024 and are heavily concentrated in the Eastern
  half of the city. In total, more than 23,600 structures are estimated to have been
  damaged or destroyed in these areas. Out of these 23,600 structures, approximately
  2,000 were found damaged before 9 May 2024; 9,500 between 9 May and 23 May 2024;
  over 4,600 between 23 May and 1 June 2024; 3,900 between 1 June and 12 June 2024;
  600 between 12 June 2024 and 26 June 2024; and 2,900 between 26 June 2024 and 31
  July 2024. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/el-fasher-damage-assessment-overview]'
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
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Fire detections from MODIS and VIIRS satellites during May 9-20, 2024
    were identified in El Fasher. UNOSAT analysts then conducted detailed satellite
    imagery analysis, comparing pre- and post-event imagery to assess structural damage
    and confirm burning indicators in residential areas. Damaged structures were mapped
    and compiled into a shapefile with geographic coordinates and assessment dates.
  sources:
  - id: source_1
    license: null
    name: MODIS satellite sensor
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: VIIRS satellite sensor
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: UNOSAT satellite imagery analysis
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/el-fasher-damage-assessment-overview
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from wildfire in El Fasher, North Darfur assessed
      through satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
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
  description: Sudan - El Fasher Damage Assessment Overview (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3913/ElFasher_DA_20240731.zip
  format: null
  id: resource_96ea61bb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ElFasher_DA_20240731.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-sdn_unosat_elfasherdamageassessmento_20240814
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
  start: '2024-08-14'
temporal_resolution: null
title: Sudan - El Fasher Damage Assessment Overview
version: null
vulnerability: null
---
