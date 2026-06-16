---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/yemen-displacement-data-area-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/yemen-displacement-data-area-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/yemen-displacement-data-area-assessment-iom-dtm
dataset_id: rdls_el-yem_iom_displacementdataareaasses_20181130
description: 'The aim of the Sub-Area Assessment is to track and monitor IDP and returnee
  populations in Yemen. Information is collected on population size, area of origin,
  current location, duration of displacement, shelter types, priority needs and movement
  trends. Among the main outputs of the Sub-Area Assessment, is a list of locations
  where IDPs and/or returnees are present that can be used to inform more detailed
  assessments at the location level, including the annual Multi-Cluster Location Assessment
  (MCLA). DTM field staff, along with KIs, use the Sub-Area Assessment tool to capture
  locations, which are matched to the identified locations in the OCHA Common Operational
  Dataset (P-Codes).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yemen-displacement-data-area-assessment-iom-dtm]'
details: null
exposure:
- asset_type:
    description: Internally displaced persons (IDPs) and returnee populations tracked
      by location, origin, and displacement duration
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
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM field staff and key informants conduct sub-area assessments
    to identify and enumerate IDP and returnee populations across Yemen, recording
    location, origin, displacement duration, shelter types, and priority needs. Data
    is aggregated at the area level to inform multi-cluster location assessments and
    humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/yemen-displacement-data-area-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displacement of populations due to conflict and violence in Yemen
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This assessment covers all 22 governorates and 333 districts. As of
    November 2018, DTM Yemen estimates that there are 3.6 million internally displaced
    persons (IDPs) and 607,865 households. The dataset also contains IDPs, Returnees
    by year at sub-national level and their needs.
  download_url: https://data.humdata.org/dataset/891f3f4f-091e-4856-9d93-e08193f4c219/resource/40b9b069-9695-457f-81d4-0b8d975f4cbb/download/dtm-yemen-area-assessment-round-37.xlsx
  format: null
  id: resource_40b9b069
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Area Assessment Round 37
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-yem_iom_displacementdataareaasses_20181130
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-11-30'
temporal_resolution: null
title: Yemen Displacement Data - Area Assessment [IOM DTM]
version: null
vulnerability: null
---
