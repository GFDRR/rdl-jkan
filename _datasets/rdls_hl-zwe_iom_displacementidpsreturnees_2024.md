---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/zimbabwe-2023-4-drought-displacement-idps-returnees-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/zimbabwe-2023-4-drought-displacement-idps-returnees-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/zimbabwe-2023-4-drought-displacement-idps-returnees-baseline-assessment-iom-dtm
dataset_id: rdls_hl-zwe_iom_displacementidpsreturnees_2024
description: 'The dataset includes internally displaced persons (IDPs) and returnees
  at the sub-national level, along with information on the reasons for displacement,
  places of origin, and dates of multiple displacements. In the context of Zimbabwe''s
  drought response, displacement dynamics remain complex and evolving. Reports indicate
  movements of IDPs from drought-affected regions to areas with better access to water
  and resources. While some individuals have permanently resettled, others frequently
  move between their place of displacement and their area of origin.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/zimbabwe-2023-4-drought-displacement-idps-returnees-baseline-assessment-iom-dtm]'
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
license: CC-BY-4.0
lineage:
  description: "IOM DTM conducted baseline assessments of internally displaced persons\
    \ and returnees across Zimbabwe's administrative divisions using standardized\
    \ survey methodology. Data collection captured displacement dynamics triggered\
    \ by drought (El Ni\u221A\xB1o-related), including origin locations, destination\
    \ areas, timing of movements, demographic composition, and priority needs. The\
    \ dataset documents both permanent resettlement and cyclical displacement patterns\
    \ between drought-affected regions and areas with better resource access."
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
- href: https://data.humdata.org/dataset/zimbabwe-2023-4-drought-displacement-idps-returnees-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (IDPs) and returnees displaced due to
      drought in Zimbabwe, with demographic breakdown by age and gender
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
    places of origin, and dates of multiple displacements. In the context of Zimbabwe's
    drought response, displacement dynamics remain complex and evolving. Reports indicate
    movements of IDPs from drought-affected regions to areas with better access to
    water and resources. While some individuals have permanently resettled, others
    frequently move between their place of displacement and their area of origin.
    Between October 19 and December 06, 2024, DTM team in Zimbabwe has identified
    189,005 individuals representing 61,721 households, including 45,799 internally
    displaced persons, 92578 absent residents departed in country and 50,628 internal
    returnees.
  download_url: https://data.humdata.org/dataset/76e5fa42-55d3-492f-a2d0-a8790dfe4cc7/resource/9b27659b-2edd-4f20-8e56-e7517063deb7/download/dtm_zimbabwe_el-nino_research-data_december-2024_hdx.xlsx
  format: null
  id: resource_9b27659b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM_Zimbabwe_El Nino_Research Data_December 2024_hdx.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-zwe_iom_displacementidpsreturnees_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - ZWE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-06'
  start: '2024-10-19'
temporal_resolution: null
title: Zimbabwe Displacement - [IDPs, Returnees] - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
