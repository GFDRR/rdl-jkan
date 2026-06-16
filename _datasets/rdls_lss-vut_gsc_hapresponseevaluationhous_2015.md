---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Shelter Cluster
    url: https://data.humdata.org/dataset/hap-shelter-cluster-response-evaluation-household-dataset
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Global Shelter Cluster (inactive)
  url: https://data.humdata.org/dataset/hap-shelter-cluster-response-evaluation-household-dataset
creator:
  affiliation: null
  email: null
  name: Global Shelter Cluster (inactive)
  url: https://data.humdata.org/dataset/hap-shelter-cluster-response-evaluation-household-dataset
dataset_id: rdls_lss-vut_gsc_hapresponseevaluationhous_2015
description: 'Following the completion of shelter activities outlined in the Humanitarian
  Action Plan (HAP) and the beginning of the transition from the emergency phase to
  longer term preparedness / recovery programming, the Shelter Cluster redeployed
  the baseline assessment team in August 2015 in order to conduct a detailed evaluation
  of the shelter response. The overall objective of the evaluation was to inform 1)
  an evaluation of the effectiveness of the shelter operational response detailed
  in the humanitarian action plan (2) identify barriers to recovery.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hap-shelter-cluster-response-evaluation-household-dataset]'
details: The overall confidence level of 90% and the margin of error of 10% correspond
  to indicators which are calculated from the full sample at the island / site level.
  Any findings calculated based on specific sub-sets of the population invariably
  have a lower confidence level. As such, findings calculated on this basis should
  only be considered as indicative.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Baseline assessment team conducted a sample survey-based household
    evaluation in August 2015 following completion of shelter cluster emergency response
    activities. The evaluation collected detailed household-level data on shelter
    conditions and recovery status to assess the effectiveness of the humanitarian
    shelter response and identify barriers to longer-term recovery.
  sources:
  - id: source_1
    license: null
    name: Global Shelter Cluster
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hap-shelter-cluster-response-evaluation-household-dataset
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Post-event shelter response evaluation capturing household-level
      impacts from cyclone
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu - HAP Shelter Cluster Response Evaluation - Household Dataset
    (Excel)
  download_url: https://data.humdata.org/dataset/224bc8f5-67dd-4231-8dbc-ae37f3eae13e/resource/9611c10e-a94f-4915-91ba-3d2bcd307d29/download/shelterclustervutevaluationassessmentmasterdbsharing.xlsx
  format: null
  id: resource_9611c10e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ShelterCluster_VUT_EvaluationAssessment_Master_DB_sharing.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-vut_gsc_hapresponseevaluationhous_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-09-04'
  start: '2015-08-17'
temporal_resolution: null
title: Vanuatu - HAP Shelter Cluster Response Evaluation - Household Dataset
version: null
vulnerability: null
---
