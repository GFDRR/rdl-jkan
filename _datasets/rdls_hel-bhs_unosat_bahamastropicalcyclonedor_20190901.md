---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/bahamas-tropical-cyclone-dorian-19-population-exposure-report
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/bahamas-tropical-cyclone-dorian-19-population-exposure-report
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/bahamas-tropical-cyclone-dorian-19-population-exposure-report
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/bahamas-tropical-cyclone-dorian-19-population-exposure-report
dataset_id: rdls_hel-bhs_unosat_bahamastropicalcyclonedor_20190901
description: 'Based on data of the observed and predicted tropical cyclone path, wind
  speeds, and population data (from WorldPop) acquired on the 1st of September 2019,
  UNITAR-UNOSAT conducted a population exposure analysis for Bahamas where about 72,000
  people will be potentially exposed to sustained winds with more than 120 km/h..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/bahamas-tropical-cyclone-dorian-19-population-exposure-report]'
details: null
exposure:
- asset_type:
    description: Population from WorldPop exposed to tropical cyclone wind speeds
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
  - analysis_type: deterministic
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
  description: UNOSAT integrated observed and predicted tropical cyclone Dorian track
    and wind speed data with WorldPop gridded population distribution to conduct a
    GIS-based population exposure analysis, quantifying the number of people potentially
    exposed to sustained winds exceeding 120 km/h across the Bahamas as of 1 September
    2019.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/bahamas-tropical-cyclone-dorian-19-population-exposure-report
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposure to sustained winds exceeding 120 km/h from tropical
      cyclone Dorian
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
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  description: Bahamas-Tropical Cyclone Dorian-19 - Population exposure report (TC
    Dorian - Population exposure report)
  download_url: https://data.humdata.org/dataset/addc33ab-d442-4867-b36e-62da117ce9b7/resource/376ee90b-be3f-461f-a6cd-cbd80ea38b09/download/unosat_pop_exposure_analysis_bahamas_20190901.pdf
  format: null
  id: resource_376ee90b
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PoP_Exposure_Analysis_Bahamas_20190901.pdf
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bhs_unosat_bahamastropicalcyclonedor_20190901
spatial:
  bbox: null
  centroid: null
  countries:
  - BHS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-09-01'
temporal_resolution: null
title: Bahamas-Tropical Cyclone Dorian-19 - Population exposure report
version: null
vulnerability: null
---
