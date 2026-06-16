---
attributions:
- entity:
    affiliation: null
    email: null
    name: Assistance Coordination Unit (ACU)
    url: https://data.humdata.org/dataset/winter-needs-in-northern-syria-camps-2021
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Assistance Coordination Unit
  url: https://data.humdata.org/dataset/winter-needs-in-northern-syria-camps-2021
creator:
  affiliation: null
  email: null
  name: Assistance Coordination Unit
  url: https://data.humdata.org/dataset/winter-needs-in-northern-syria-camps-2021
dataset_id: rdls_el-syr_acu_winterneedsnortherncamps2_2021
description: 'The IMU of the ACU, issues its fourth edition of the ''Winter Needs
  in the Northern Syrian Camps'' report, addressing 680 camps in the governorates
  of Aleppo and Idleb. The report brings to light the most important items that IDPs
  are in need for in terms of type and quantities, according to international standards
  for humanitarian response. It furthermore, brings emphasis to bear on the course
  of action that IDPs, as well as the camp management teams, should follow to drive
  down the effects of natural disasters that may put their lives at risk. Noting that
  the number of families that ACU enumerators were able to assess their needs reached
  156,873 families, making up an overall individual number of 872,082 IDPs. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/winter-needs-in-northern-syria-camps-2021]'
details: null
exposure:
- asset_type:
    description: Internally displaced persons (IDPs) living in 680 camps across Aleppo
      and Idleb governorates
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
  description: Sample survey conducted by ACU's Information Management Unit across
    680 IDP camps in Aleppo and Idleb governorates to enumerate winter needs and disaster
    risk awareness. Data collected according to international humanitarian response
    standards to identify required non-food items and shelter needs for vulnerable
    populations exposed to winter conditions and natural hazards.
  sources:
  - id: source_1
    license: null
    name: Assistance Coordination Unit (ACU)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/winter-needs-in-northern-syria-camps-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Winter needs assessment for IDP populations vulnerable to extreme
      cold conditions
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: null
      trigger: null
      type: extreme_temperature
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
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
  description: Winter needs in Northern Syria Camps 2021 (Excel)
  download_url: https://data.humdata.org/dataset/be71e3e9-e07a-49e4-9ed0-d16d22722fd4/resource/bb124eb5-6c42-4f86-bcf8-0accad464999/download/acu_syria_winter_needs_in_northers_syria_camps_october_2021.xlsx
  format: null
  id: resource_bb124eb5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ACU_Syria_Winter_Needs_In_Northers_Syria_Camps_October_2021.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_acu_winterneedsnortherncamps2_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-11-01'
  start: '2021-10-01'
temporal_resolution: null
title: Winter needs in Northern Syria Camps 2021
version: null
vulnerability: null
---
