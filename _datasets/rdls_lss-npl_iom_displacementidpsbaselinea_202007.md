---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/nepal-displacement-idps-baseline-assessment-floods2020-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/nepal-displacement-idps-baseline-assessment-floods2020-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/nepal-displacement-idps-baseline-assessment-floods2020-iom-dtm
dataset_id: rdls_lss-npl_iom_displacementidpsbaselinea_202007
description: 'Large-scale flooding and landslides have been triggered in several districts
  across Nepal following heavy rainfalls in July 2020. From the onset of monsoon on
  12 June until 25 July, 130 people lost their lives, 115 were injured and 51 went
  missing due to floods and landslides according to the National Disaster Risk Reduction
  and Management Authority.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/nepal-displacement-idps-baseline-assessment-floods2020-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event impact data collected by IOM through DTM standard methodology
    following heavy monsoon rainfall (12 June - 25 July 2020) that triggered widespread
    flooding and landslides across multiple districts in Nepal. The dataset documents
    verified casualty figures (deaths, injuries, missing persons) and displacement
    counts reported by the National Disaster Risk Reduction and Management Authority
    and field assessments.
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
- href: https://data.humdata.org/dataset/nepal-displacement-idps-baseline-assessment-floods2020-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Flood-related fatalities from July 2020 monsoon flooding in Nepal
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Flood-related injuries from July 2020 monsoon flooding in Nepal
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from July 2020 monsoon flooding in Nepal
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
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
    description: Landslide-related fatalities from July 2020 monsoon-triggered landslides
      in Nepal
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Landslide-related injuries from July 2020 monsoon-triggered landslides
      in Nepal
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
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
  description: The baseline assessment was carried out from 15 to 24 July in five
    remote hilly districts namely Jajarkot, Sindhupalchowk, Gulmi, Shankhuwasabha
    and Myagdi to identify and verify locations where displaced persons are residing
    in temporary settlements. It is estimated that around 13, 352 individuals are
    displaced and are living in 65 active sites spread across 5 districts, 11 rural
    and urban municipalities and 31 wards.
  download_url: https://data.humdata.org/dataset/355e2730-00fb-4760-a756-a63f274e66d4/resource/8a75dfd8-93ee-42ea-ad28-f5f77b898120/download/dtm-nepal-baseline-assessment-floods20-r1.xlsx
  format: null
  id: resource_8a75dfd8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Nepal Baseline Assessment Floods20 R1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_iom_displacementidpsbaselinea_202007
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-07-24'
  start: '2020-07-15'
temporal_resolution: null
title: Nepal Displacement - [IDPs] - Baseline Assessment - Floods2020 - [IOM DTM]
version: null
vulnerability: null
---
