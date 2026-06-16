---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNITAR-UNOSAT
    url: https://data.humdata.org/dataset/damage-assessment-in-barbuda-island-as-of-8-september-2017
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian Open Street Map
    url: https://data.humdata.org/dataset/damage-assessment-in-barbuda-island-as-of-8-september-2017
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-barbuda-island-as-of-8-september-2017
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-barbuda-island-as-of-8-september-2017
dataset_id: rdls_hl-atg_unosat_damageassessmentbarbudais_20170908
description: 'This dataset illustrates satellite-detected potential damaged buildings
  in Barbuda Island following the landfall of Tropical Cyclone IRMA-17 on September
  6, 2017. The UNITAR-UNOSAT analysis used a Pleiades satellite image acquired on
  8 September 2017 as post imagery. The UNITAR-UNOSAT analysis identified 1,071 potentially
  damaged structures within Codrington town in Barbuda. According to the pre-building
  footprints provided by Humanitarian Open Street Map, this represents 89% of potentially
  affected structures in Codrington town. The analysis could have been underestimated
  due to cloud cover. This is a preliminary analysis and has not yet been validated
  in the field.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-barbuda-island-as-of-8-september-2017]'
details: This is a preliminary analysis and has not yet been validated in the field.
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Post-event damage assessment derived from Pleiades satellite imagery
    acquired 8 September 2017, compared against pre-event building footprints from
    Humanitarian Open Street Map to identify and count potentially damaged structures
    in Codrington town, Barbuda following Tropical Cyclone IRMA-17 landfall on 6 September
    2017.
  sources:
  - id: source_1
    license: null
    name: UNITAR-UNOSAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian Open Street Map
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-barbuda-island-as-of-8-september-2017
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected potentially damaged buildings (1,071 structures)
      in Codrington town following Tropical Cyclone IRMA-17
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
        metric: loss
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Antigua and Barbuda - Damage Assessment in Barbuda Island as of 8 September
    2017 (Shapefile)
  download_url: https://data.humdata.org/dataset/f894e4ee-eb01-4f17-bd07-8142d78f6f2e/resource/f48abf3a-3c69-4e47-8636-f32b8c0f8d9d/download/barbuda_building_damage_assessment_8sept.zip
  format: null
  id: resource_f48abf3a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Barbuda_building_damage_assessment_8sept.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-atg_unosat_damageassessmentbarbudais_20170908
spatial:
  bbox: null
  centroid: null
  countries:
  - ATG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-09-08'
temporal_resolution: null
title: Antigua and Barbuda - Damage Assessment in Barbuda Island as of 8 September
  2017
version: null
vulnerability: null
---
