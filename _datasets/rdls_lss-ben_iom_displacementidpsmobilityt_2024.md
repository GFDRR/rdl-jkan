---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/benin-displacement-idps-mobility-tracking-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/benin-displacement-idps-mobility-tracking-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/benin-displacement-idps-mobility-tracking-iom-dtm
dataset_id: rdls_lss-ben_iom_displacementidpsmobilityt_2024
description: 'Due to Sahel Crisis, IOM DTM conducted mobility tracking in Alibori
  and Atacora departments in Benin. The datasets show the total number of IDP individuals
  identified and the origin of the majority of IDPs.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/benin-displacement-idps-mobility-tracking-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted field-based mobility tracking surveys in Alibori
    and Atacora departments of Benin following the Sahel crisis. Enumerators interviewed
    community leaders and key informants at locality level to identify total IDP counts,
    household numbers, displacement reasons (climate-related and conflict-related),
    origin locations, and temporal dynamics. Data were collected across multiple survey
    rounds (Round 2 and Round 3) and disaggregated by gender and age.
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
- href: https://data.humdata.org/dataset/benin-displacement-idps-mobility-tracking-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons identified through mobility tracking
      in response to Sahel crisis (conflict and climate-related hazards)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Internally displaced persons identified through mobility tracking
      in response to drought and climate-related hazards
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://displacement.iom.int/sites/default/files/public/Methodological%20Framework%20used%20in%20DTM%20Operations%20for%20Quantifying%20Displacement%20and%20Mobility.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains the results of displacement tracking activities
    conducted in the north of the country. The assessment was carried out in 254 localities
    hosting internally displaced persons (IDPs). Data collection took place from 16
    to 22 July 2025 in the 11 communes of the Alibori and Atakora departments.
  download_url: https://data.humdata.org/dataset/b32b1739-ba36-4cc6-9c62-93b0d4a89846/resource/53fc119d-0c2b-4a39-afc0-8ad1329ee4e0/download/iom_dtm_benin_mt_baseline_assessment_round_3_hdx.xlsx
  format: null
  id: resource_53fc119d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Benin - Mobility Tracking - Round 3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In round 2, 12,501 IDP individuals were identified. Among them, 4,564
    were children under 18 years old.
  download_url: https://data.humdata.org/dataset/b32b1739-ba36-4cc6-9c62-93b0d4a89846/resource/37eefd7d-794f-42e0-8a06-a0c9fa126388/download/ben_mt_clean_final_publish_hdx.xlsx
  format: null
  id: resource_37eefd7d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Benin - Mobility Tracking - Round 2
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ben_iom_displacementidpsmobilityt_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - BEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-07-22'
  start: '2024-02-05'
temporal_resolution: null
title: Benin Displacement - [IDPs] - Mobility Tracking [IOM DTM]
version: null
vulnerability: null
---
