---
attributions:
- entity:
    affiliation: null
    email: null
    name: South Africa Red Cross Society
    url: https://data.humdata.org/dataset/south-africa-displacement-data-baeline-ward-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/south-africa-displacement-data-baeline-ward-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/south-africa-displacement-data-baeline-ward-assessment-iom-dtm
dataset_id: rdls_hl-zaf_iom_displacementdatabaselinew_202206
description: 'Dataset has IDPs, Households, challenges faced by IDPs etc. On 11-13
  April, severe flooding and landslides caused by heavy rainfall affected southern
  and south-eastern South Africa. In response to the need for accurate information
  on internally displaced persons (IDPs) in South Africa, the International Organization
  for Migration (IOM) in partnership with the South Africa Red Cross Society and in
  coordination with provincial and local authorities, deployed teams from June 2022
  to conduct baseline assessments at ward level. The project is supporting the Government
  of South Africa and other humanitarian response partners to conduct IDPs assessments
  in a systematic way as well as to establish a profile of the IDP population.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/south-africa-displacement-data-baeline-ward-assessment-iom-dtm]'
details: null
exposure: []
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: In response to severe flooding and landslides triggered by heavy rainfall
    in southern and south-eastern South Africa on 11-13 April 2022, IOM in partnership
    with the South Africa Red Cross Society and provincial/local authorities deployed
    assessment teams from June 2022 onwards to conduct baseline ward-level surveys
    of internally displaced persons using DTM methodology. The dataset captures IDP
    counts, household information, and reported challenges at the ward administrative
    level.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: South Africa Red Cross Society
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-africa-displacement-data-baeline-ward-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flooding and landslides assessed
      at ward level
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from landslides assessed at ward level
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'On 11-13 April, severe flooding and landslides caused by heavy rainfall
    affected southern and south-eastern South Africa, particularly the provinces of
    KwaZulu-Natal and Eastern Cape. According to national authorities, at least 123,808
    people were affected, 448 people died and over 30,000 are displaced, mostly in
    collective evacuation centres. The devastation in the most affected areas of KwaZulu-Natal
    and Eastern Cape provinces is immense: nearly 12,500 homes have been destroyed
    or damaged, 66 health centres affected, and 600 schools devastated which will
    put 270,000 students at risk. A National State of Disaster has been declared in
    response to the floods and landslides, and rescue teams have been deployed to
    the affected areas to provide humanitarian assistance to those most affected.
    To better assist authorities and partners to respond to the situation, IOM in
    partnership with the South Africa Red Cross Society and in coordination with provincial
    and local authorities, deployed teams from 13 to 17 June to conduct baseline assessments
    at ward level. These assessments provide a snapshot of the number of displaced
    persons residing in 26 of the most affected wards in Ethekwini district. The assessments
    also provide an overview of the sectoral needs, gaps and potential solutions,
    including water and sanitation (WASH), food security, health, infrastructure and
    protection. Finally, a list of priority locations for further assessment were
    identified.'
  download_url: https://data.humdata.org/dataset/4fcca449-1751-4560-b7ac-5d207ab53480/resource/e324caa4-9152-4cc3-9cd7-228335e06632/download/hdx_ward_baseline_assessment_kzn2022.xlsx
  format: null
  id: resource_e324caa4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: South Africa - Baseline Ward Assessment - Round 1
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-zaf_iom_displacementdatabaselinew_202206
spatial:
  bbox: null
  centroid: null
  countries:
  - ZAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-06-17'
  start: '2022-06-13'
temporal_resolution: null
title: South Africa Displacement Data - Baseline Ward Assessment [IOM DTM]
version: null
vulnerability: null
---
