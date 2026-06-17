---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Programa Presidencial para la Acci\xF3n Integral contra Minas Antipersonal"
    url: https://data.humdata.org/dataset/explosive-remnants-of-war-in-colombia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/explosive-remnants-of-war-in-colombia
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/explosive-remnants-of-war-in-colombia
dataset_id: rdls_hl-col_ochacol_explosiveremnantswar19822_20140202
description: 'Data on ERG accidents and events, mostly involving antipersonnel mines,
  by municipality between 1982 and December 2013. Accident data is defined as events
  resulting in injury or death. Event data includes both accidents and other events
  such as ERG detection or minefield deactivation. This data is also available online
  and updated, at http://www.accioncontraminas.gov.co/Paginas/AICMA.aspx. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/explosive-remnants-of-war-in-colombia]'
details: Georeferencing in this dataset is only available to the municipal level.
  Georeferencing by defect is made at the municipal seat coordinates, although most
  events or accidents occur in rural areas of the municipality. Some of this same
  data is also available with more precise georeferencing, but not in this dataset.
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
      intensity_measure: Pest:count/area
      process: pest
      trigger: null
      type: pest_infestation
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: pest_infestation
license: CC0-1.0
lineage:
  description: Post-event registry data compiled by the Colombian Presidential Program
    for Comprehensive Action Against Antipersonnel Mines, documenting all recorded
    ERG accidents (resulting in injury or death) and detection/deactivation events
    by municipality from 1982 through December 2013.
  sources:
  - id: source_1
    license: null
    name: "Programa Presidencial para la Acci\xF3n Integral contra Minas Antipersonal"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/explosive-remnants-of-war-in-colombia
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Injuries from antipersonnel mine accidents
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
        metric: ppl_injured
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Fatalities from antipersonnel mine accidents
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
        metric: casualty_count
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Explosive Remnants of War in Colombia, 1982-2013 (See description and
    caveats.)
  download_url: https://data.humdata.org/dataset/b6d4823e-af32-4549-a9d0-598057d0405a/resource/8cb71bd4-572d-43be-8772-c5313b4745b9/download/situacion-minas-diciembre-2013.xls
  format: null
  id: resource_8cb71bd4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Situaci\xF3n_Minas_Diciembre_2013.xls"
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-col_ochacol_explosiveremnantswar19822_20140202
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-02-02'
temporal_resolution: null
title: Explosive Remnants of War in Colombia, 1982-2013
version: null
vulnerability: null
---
