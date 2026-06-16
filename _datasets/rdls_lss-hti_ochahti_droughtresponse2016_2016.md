---
attributions:
- entity:
    affiliation: null
    email: null
    name: National coordination of Food Security (CNSA)
    url: https://data.humdata.org/dataset/drought-response-in-haiti-2016
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/drought-response-in-haiti-2016
creator:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/drought-response-in-haiti-2016
dataset_id: rdls_lss-hti_ochahti_droughtresponse2016_2016
description: 'List of projects being developed currently in Haiti in the context of
  the drought response. The data of this document was collected only for 4 towns,
  that are considered to be in IPC phase 3 by the National coordination of Food Security
  (CNSA) The dataset contains the list of projects organized by sectors: Food Security,
  Agriculture, Nutrition and WASH. The document also contains the estimated populations
  in need by commune and sector. The caseload for the nutrition projects corresponds
  only to children under five years old. An analysis document developed with this
  data is available at: https://goo.gl/NBHRZI. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/drought-response-in-haiti-2016]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: This dataset is a humanitarian response project registry compiled by
    OCHA Haiti documenting interventions across Food Security, Agriculture, Nutrition,
    and WASH sectors in response to the 2016 drought. Population needs estimates by
    commune and sector were derived from IPC phase 3 classifications assigned by CNSA,
    with nutrition caseloads specifically targeting children under five. The registry
    serves to track humanitarian response activities and resource allocation in drought-affected
    areas.
  sources:
  - id: source_1
    license: null
    name: National coordination of Food Security (CNSA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/drought-response-in-haiti-2016
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated populations in need by commune affected by drought in IPC
      phase 3
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Drought Response in Haiti 2016 (Projets Reponse Secheresse 2016 _ HDX.xlsx)
  download_url: https://data.humdata.org/dataset/126d4d95-87d8-4440-b4d4-e51e7d0c32fc/resource/a1fee4d8-4335-45ca-a80b-19a7bc01a7dc/download/projets-reponse-secheresse-2016-_-hdx.xlsx
  format: null
  id: resource_a1fee4d8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Projets Reponse Secheresse 2016 _ HDX.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_ochahti_droughtresponse2016_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-12-31'
  start: '2016-06-01'
temporal_resolution: null
title: Drought Response in Haiti 2016
version: null
vulnerability: null
---
