---
attributions:
- entity:
    affiliation: null
    email: null
    name: Assistance Coordination Unit (ACU)
    url: https://data.humdata.org/dataset/syria-earthquake-injury-assessment
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Assistance Coordination Unit
  url: https://data.humdata.org/dataset/syria-earthquake-injury-assessment
creator:
  affiliation: null
  email: null
  name: Assistance Coordination Unit
  url: https://data.humdata.org/dataset/syria-earthquake-injury-assessment
dataset_id: rdls_lss-syr_acu_earthquakeinjuryassessmen_2023
description: 'The recent earthquake that struck the south of Turkey and the north
  of Syria on the 6th of February has caused widespread destruction and devastation
  in the region. Thousands of people lost their lives, and many more were injured.
  The aftermath of this disaster has left many families displaced and in desperate
  need of medical attention. In response to this crisis, the Assistance Coordination
  Unit (ACU) conducted a survey in health facilities in northwest Syria to assess
  epidemiologically earthquake-induced injuries in northwest Syria. This report aims
  to present this survey''s findings and provide insights into the types of injuries
  sustained by individuals affected by the earthquake using the International Statistical
  Classification of Diseases and Related Health Problems, 10th revision (ICD 10).
  This report highlights the urgent need for medical aid and support in the affected
  areas to prevent further loss of life and alleviate the suffering of those impacted
  by this tragic event.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/syria-earthquake-injury-assessment]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The Assistance Coordination Unit conducted a direct observational survey
    of health facilities in northwest Syria to epidemiologically assess earthquake-induced
    injuries following the 6 February 2023 Turkey-Syria earthquake. Survey findings
    on injury counts and characteristics were compiled into an assessment report.
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
- href: https://data.humdata.org/dataset/syria-earthquake-injury-assessment
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct injuries to population from earthquake ground motion
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Syria Earthquake Injury Assessment 23 March 2023.xlsx
  download_url: https://data.humdata.org/dataset/e4220f7a-587d-4111-a0b4-fb7640856bd9/resource/7dce0820-8fd2-4f2c-a82b-99c2475bb64a/download/syria-earthquake-injury-assessment-23-march-2023.xlsx
  format: null
  id: resource_7dce0820
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Syria Earthquake Injury Assessment 23 March 2023.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_acu_earthquakeinjuryassessmen_2023
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
  end: '2023-04-04'
  start: '2023-03-01'
temporal_resolution: null
title: Syria Earthquake Injury Assessment
version: null
vulnerability: null
---
