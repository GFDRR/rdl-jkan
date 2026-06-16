---
attributions:
- entity:
    affiliation: null
    email: null
    name: ACTED
    url: https://data.humdata.org/dataset/reach-afghanistan-post-earthquake-shelter-evaluation
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: AfghanAid
    url: https://data.humdata.org/dataset/reach-afghanistan-post-earthquake-shelter-evaluation
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: People in Need
    url: https://data.humdata.org/dataset/reach-afghanistan-post-earthquake-shelter-evaluation
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/reach-afghanistan-post-earthquake-shelter-evaluation
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/reach-afghanistan-post-earthquake-shelter-evaluation
dataset_id: rdls_lss-afg_reach_postearthquakesheltereval_20160831
description: 'On the 26th of October 2015, a large scale earthquake caused shelter
  damage throughout much of northern and central Afghanistan. During August 2016,
  the REACH Initiative (supported by ACTED, AfghanAid and People in Need) conducted
  a shelter response evaluation in 3 districts of Afghanistan on behalf of the Shelter
  Cluster. The aim of the assessment was to evaluate shelter interventions and locate
  possible intervention gaps in order to inform the shelter cluster of Afghanistan
  of the current shelter context and needs of earthquake affected families. The assessment
  consisted of three specific areas of investigation: 1. To monitor change in sheltering
  conditions for families 2. To evaluate the value of various shelter interventions
  in allowing families to recover and to identify possible gaps 3. To determine recovery
  limitations and successes relating to vulnerable groups. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/reach-afghanistan-post-earthquake-shelter-evaluation]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Following the October 2015 earthquake in northern and central Afghanistan,
    REACH Initiative conducted a sample survey in August 2016 across 3 districts on
    behalf of the Shelter Cluster, supported by ACTED, AfghanAid, and People in Need.
    The survey collected household-level data on shelter damage and the effectiveness
    of shelter interventions to identify gaps and inform the Afghanistan Shelter Cluster's
    response planning.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: ACTED
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: AfghanAid
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: People in Need
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/reach-afghanistan-post-earthquake-shelter-evaluation
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Post-earthquake shelter damage assessment evaluating shelter interventions
      and gaps in 3 districts of northern and central Afghanistan following the October
      2015 earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Post-Earthquake Shelter Evaluation (Data collection tool)
  download_url: https://data.humdata.org/dataset/05e0f7e7-cc6e-4bda-86a1-10e31419aa66/resource/43cebaa9-615b-4fd7-9ccd-1bfdafd96c73/download/reach_afg_tool_earthquake_shelter_evaluation_august2016.xlsx
  format: null
  id: resource_43cebaa9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reach_afg_tool_earthquake_shelter_evaluation_august2016.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Post-Earthquake Shelter Evaluation (Excel)
  download_url: https://data.humdata.org/dataset/05e0f7e7-cc6e-4bda-86a1-10e31419aa66/resource/9954b85c-8aee-422a-957c-23b226361c0b/download/reach_afg_dataset_shelter_earthquake_dec2016.xlsx
  format: null
  id: resource_9954b85c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH_AFG_dataset_Shelter_Earthquake_Dec2016.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_reach_postearthquakesheltereval_20160831
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-08-31'
temporal_resolution: null
title: Afghanistan - Post-Earthquake Shelter Evaluation
version: null
vulnerability: null
---
