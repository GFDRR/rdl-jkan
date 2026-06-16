---
attributions:
- entity:
    affiliation: null
    email: null
    name: The Cambodian Mine Action and Victim Assistance Authority (CMAA)
    url: https://data.humdata.org/dataset/cambodia-protection-0
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: The Cambodia Mine/ERW Victim Information System (CMVIS)
    url: https://data.humdata.org/dataset/cambodia-protection-0
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/cambodia-protection-0
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/cambodia-protection-0
dataset_id: rdls_lss-khm_ocharoap_casualtyincident_20130101
description: 'Casualty Incident by ERW/Mine. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cambodia-protection-0]'
details: '**Languages:** EN'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Casualty incident data compiled from the Cambodia Mine/ERW Victim Information
    System (CMVIS) maintained by the Cambodian Mine Action and Victim Assistance Authority
    (CMAA), covering recorded deaths and injuries from mine and ERW incidents during
    2005-2013, georeferenced as point locations.
  sources:
  - id: source_1
    license: null
    name: The Cambodian Mine Action and Victim Assistance Authority (CMAA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: The Cambodia Mine/ERW Victim Information System (CMVIS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cambodia-protection-0
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Casualty fatalities from explosive remnants of war (ERW) and mine
      incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_pest_infestation
      intensity_measure: Pest:count/area
      process: null
      trigger: null
      type: pest_infestation
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Casualty injuries from explosive remnants of war (ERW) and mine incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_pest_infestation
      intensity_measure: Pest:count/area
      process: null
      trigger: null
      type: pest_infestation
    id: loss_2
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cambodia - Casualty Incident (Shapefile)
  download_url: https://data.humdata.org/dataset/42bb25d2-66b4-49c8-bbcf-542e2910ca8c/resource/e8171489-3787-4af2-ae11-80ab8281061d/download/khm_casualtyincidentp_gov_cmaa_cmvis_2005_2013.zip
  format: null
  id: resource_e8171489
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: khm_casualtyincidentp_gov_cmaa_cmvis_2005_2013.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-khm_ocharoap_casualtyincident_20130101
spatial:
  bbox: null
  centroid: null
  countries:
  - KHM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2013-01-01'
temporal_resolution: null
title: Cambodia - Casualty Incident
version: null
vulnerability: null
---
