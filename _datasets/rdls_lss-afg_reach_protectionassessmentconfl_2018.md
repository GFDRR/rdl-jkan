---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/afghanistan-protection-assessment-of-conflict-affected-populations-may-2018
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/afghanistan-protection-assessment-of-conflict-affected-populations-may-2018
dataset_id: rdls_lss-afg_reach_protectionassessmentconfl_2018
description: 'The overall objective of the assessment was to inform humanitarian intervention
  planning through the identification of key protection-based needs and vulnerabilities
  of conflict-affected populations, specifically focusing on the impact conflict has
  on these needs and vulnerabilities.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-protection-assessment-of-conflict-affected-populations-may-2018]'
details: 'REACH would like to acknowledge the contribution of the following partners
  that supported the planning and data collection of this assessment: OCHA, ACTED,
  Humanitarian Access Group, Afghanistan Protection Cluster, and the GBV, CPiE, MA,
  and HLP Sub-Clusters. Raw data set and cleaning log are available upon request.'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Sample survey conducted by REACH Initiative in May 2018 to assess protection-based
    needs and vulnerabilities of conflict-affected populations in Afghanistan, with
    focus on displacement and protection impacts from armed conflict.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-protection-assessment-of-conflict-affected-populations-may-2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Protection needs and vulnerabilities of conflict-affected populations
      including IDPs, refugees, and returnees
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Displacement impacts from armed conflict on affected populations
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
  description: The overall objective of the assessment was to inform humanitarian
    intervention planning through the identification of key protection-based needs
    and vulnerabilities of conflict-affected populations, specifically focusing on
    the impact conflict has on these needs and vulnerabilities.
  download_url: https://data.humdata.org/dataset/18ceae6f-5713-4b67-b9c5-7b68a60ff311/resource/de3a32f6-ced4-48e7-8148-27a684d0751a/download/reach_afg_dataset_protection_assessment_of_conflict_affected_populations_may2018.xlsx
  format: null
  id: resource_de3a32f6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH_AFG_Dataset_Protection_Assessment_of_Conflict_Affected_Populations_May2018.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_reach_protectionassessmentconfl_2018
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
  end: '2018-05-03'
  start: '2018-03-18'
temporal_resolution: null
title: Afghanistan Protection Assessment of Conflict Affected Populations May 2018
version: null
vulnerability: null
---
