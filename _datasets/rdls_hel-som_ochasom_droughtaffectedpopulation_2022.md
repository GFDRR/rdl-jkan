---
attributions:
- entity:
    affiliation: null
    email: null
    name: IPC (Integrated Food Security Phase Classification)
    url: https://data.humdata.org/dataset/ocha-somalia-population-idp-pin-operational-priority-areas-access-ipc5
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FSNAU (Food Security and Nutrition Analysis Unit)
    url: https://data.humdata.org/dataset/ocha-somalia-population-idp-pin-operational-priority-areas-access-ipc5
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/ocha-somalia-population-idp-pin-operational-priority-areas-access-ipc5
creator:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/ocha-somalia-population-idp-pin-operational-priority-areas-access-ipc5
dataset_id: rdls_hel-som_ochasom_droughtaffectedpopulation_2022
description: 'Drought related data: Population IDPs Affected Population Priority Areas
  IPC 5 (Oct - Dec 2022 projection) Severity of access.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/ocha-somalia-population-idp-pin-operational-priority-areas-access-ipc5]'
details: null
exposure:
- asset_type:
    description: Population affected by drought conditions across priority areas
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
license: CC-BY-4.0
lineage:
  description: Dataset aggregates drought impact data from multiple humanitarian sources
    (OCHA, IPC, FSNAU) combining observed population displacement, food security classifications,
    and humanitarian access constraints. Direct observational and anecdotal data were
    compiled to quantify affected populations and priority areas requiring humanitarian
    intervention during the 2022 drought crisis.
  sources:
  - id: source_1
    license: null
    name: OCHA Somalia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: IPC (Integrated Food Security Phase Classification)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: FSNAU (Food Security and Nutrition Analysis Unit)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ocha-somalia-population-idp-pin-operational-priority-areas-access-ipc5
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Drought-affected population counts by administrative area and IPC
      severity classification
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
    description: Internally displaced persons (IDPs) resulting from drought conditions
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Drought related data: Population IDPs Affected Population Priority
    Areas IPC 5 (Oct - Dec 2022 projection) Severity of access'
  download_url: https://data.humdata.org/dataset/b3470d8e-cb21-4849-a587-a81f72a5ec30/resource/969b60d9-2561-40a8-b883-9ab31b84259b/download/ocha_som_drought_population_idp_pin_priority-areas_access_ipc5_2022.xlsx
  format: null
  id: resource_969b60d9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_SOM_Drought_Population_IDP_PIN_Priority-Areas_Access_IPC5_2022.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-som_ochasom_droughtaffectedpopulation_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-10-31'
  start: '2022-01-01'
temporal_resolution: null
title: Somalia - Drought Affected Populations
version: null
vulnerability: null
---
