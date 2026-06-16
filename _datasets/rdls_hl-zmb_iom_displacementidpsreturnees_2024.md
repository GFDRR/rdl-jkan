---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/zambia-displacement-idps-returnees-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/zambia-displacement-idps-returnees-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/zambia-displacement-idps-returnees-baseline-assessment-iom-dtm
dataset_id: rdls_hl-zmb_iom_displacementidpsreturnees_2024
description: 'The dataset includes internally displaced persons (IDPs) and returnees
  at the sub-national level, along with information on the reasons for displacement,
  places of origin, and dates of multiple displacements. In the context of Zambia''s
  drought response, displacement dynamics remain complex and evolving. Reports indicate
  movements of IDPs from drought-affected regions to areas with better access to water
  and resources. While some individuals have permanently resettled, others frequently
  move between their place of displacement and their area of origin.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/zambia-displacement-idps-returnees-baseline-assessment-iom-dtm]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted structured interviews at ward level across Zambia
    in December 2024 to assess displacement dynamics triggered by drought since September
    2023. Data collection captured household and individual counts of departures,
    arrivals, and returnees, along with origin/destination locations and primary displacement
    drivers. The dataset integrates spatial administrative hierarchies (Admin1-4)
    with displacement flow estimates and humanitarian needs assessments.
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
- href: https://data.humdata.org/dataset/zambia-displacement-idps-returnees-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees displaced due to drought
      in Zambia, with household and individual counts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  url: https://dtm.iom.int/sites/g/files/tmzbdl1461/files/DTM%20Methodological%20Framework%20-%202nd%20Edition%202022_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The dataset includes internally displaced persons (IDPs) and returnees
    at the sub-national level, along with information on the reasons for displacement,
    places of origin, and dates of multiple displacements. In the context of Zambia's
    drought response, displacement dynamics remain complex and evolving. Reports indicate
    movements of IDPs from drought-affected regions to areas with better access to
    water and resources. While some individuals have permanently resettled, others
    frequently move between their place of displacement and their area of origin.
    Between October 19 and December 11, 2024, DTM team in Zambia has identified 202,218
    individuals representing 40,172 households, including 140,261 internally displaced
    persons, 42,200 absent residents departed in country and 19,757 internal returnees.
  download_url: https://data.humdata.org/dataset/bf09a682-9410-46da-b05a-81079c90b657/resource/30358d1e-1a4f-47ce-8129-9b035cb1a35c/download/dtm_zambia_baseline_assessment_december_2024_hdx.xlsx
  format: null
  id: resource_30358d1e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Round_1_DTM_Zambia_Baseline_Assessment_Dec_2024
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-zmb_iom_displacementidpsreturnees_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-11'
  start: '2024-10-19'
temporal_resolution: null
title: Zambia Displacement - [IDPs, Returnees] - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
