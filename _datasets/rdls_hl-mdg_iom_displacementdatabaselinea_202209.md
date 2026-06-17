---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/madagascar-displacement-data-baseline-assessment-drought-in-grand-sud-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/madagascar-displacement-data-baseline-assessment-drought-in-grand-sud-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/madagascar-displacement-data-baseline-assessment-drought-in-grand-sud-iom-dtm
dataset_id: rdls_hl-mdg_iom_displacementdatabaselinea_202209
description: 'The Grand Sud of Madagascar has been affected by consecutive droughts
  during the rainy seasons from 2019 to 2021. In 2021, 36% of the Grand Sud was classified
  as severe drought and 1% as extreme drought. Nearly 1.47 million people were severely
  food insecure (IPC 3+) and four districts - Amboasary Atsimo, Ambovombe Androy,
  Tsihombe and Ampanihy West - were in IPC Phase 4 (Emergency).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/madagascar-displacement-data-baseline-assessment-drought-in-grand-sud-iom-dtm]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
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
  type: drought
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted a baseline sample survey in September 2022 to assess
    displacement outcomes in Grand Sud Madagascar following consecutive droughts (2019-2021).
    Survey data captured internally displaced persons, returnees, and food insecurity
    classifications (IPC phases) across four emergency-phase districts, integrating
    drought severity observations with population displacement and food security impact
    metrics.
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
- href: https://data.humdata.org/dataset/madagascar-displacement-data-baseline-assessment-drought-in-grand-sud-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population severely food insecure (IPC 3+) due to drought in Grand
      Sud
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees resulting from drought-induced
      displacement
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'The dataset presents the result of evaluations conducted in September
    2022 in 20 municipalities: Ambovombe (Ambanisarika, Maroalomainty, Maroalipoty,
    Marovato Befeno, Sihanamaro), Tsihombe (Anjapaly, Ankilivalo, Betanty, Imongy,
    Tsihombe, Amboasary Atsimo (Amboasary Atsimo, Behara, Ebelo, Ifotaka, Sampoana),
    Ampanihy Andrefana (Amboropotsy, Ampanihy Andrefana, Androka, Ankiliabo, Beahitse).'
  download_url: https://data.humdata.org/dataset/a73a71cd-c356-4f21-b6dd-8452bf5245c8/resource/0247ce98-26d6-4d87-96b5-e977138fac47/download/dtm_madagascar_baseline_assessment_round_1_sep_2022.xlsx
  format: null
  id: resource_0247ce98
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Madagascar - BA Drought in Gand Sud - Sep 2022
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mdg_iom_displacementdatabaselinea_202209
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-09-30'
  start: '2022-09-01'
temporal_resolution: null
title: Madagascar Displacement Data - Baseline Assessment - Drought in Grand Sud [IOM
  DTM]
version: null
vulnerability: null
---
