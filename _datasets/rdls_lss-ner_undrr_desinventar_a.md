---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Systeme d'Alerte Precoce (SAP)
  url: https://data.humdata.org/dataset/d16485d0-2011-4f5d-bb12-9e92feb8f853
creator:
  affiliation: null
  email: isdr@un.org
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://www.desinventar.net/
dataset_id: rdls_lss-ner_undrr_desinventar_a
description: 'National disaster loss inventory for Niger from the DesInventar Sendai
  Framework Monitor database, compiled by Systeme d''Alerte Precoce (SAP) and published
  by the United Nations Office for Disaster Risk Reduction (UNDRR). Contains 1,362
  event-level loss records covering historical, with observed impacts from drought,
  flood, wildfire events. Loss data includes human casualties, displacement, building
  damage, economic losses, agricultural damage, and infrastructure impacts. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX) at https://data.humdata.org] [Original dataset: https://data.humdata.org/dataset/d16485d0-2011-4f5d-bb12-9e92feb8f853]'
details: 'Event-level disaster loss records from the DesInventar database for Niger,
  maintained by Systeme d''Alerte Precoce (SAP). Covers 1,362 observed disaster events
  from historical. Data collected through direct observational reporting and includes
  human impacts (deaths, injuries, missing, affected, evacuated, relocated), physical
  impacts (houses destroyed/damaged, education centres, hospitals, roads), economic
  losses (local currency and USD), and agricultural impacts (crop damage in hectares,
  livestock losses). Methodology: Direct Observational Data / Anecdotal Data.'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Event-level disaster loss records collected through the DesInventar
    Sendai system, a standardised methodology for building national disaster loss
    databases developed by LA RED / UNDRR. National disaster events are documented
    through systematic review of local and national newspapers, official reports from
    civil protection agencies, national statistics offices, and other primary administrative
    sources. Each record represents a discrete observed disaster event with associated
    human impacts (deaths, injuries, missing persons, affected and evacuated populations),
    physical impacts (houses destroyed and damaged), agricultural losses (crop area
    damaged in hectares), and economic losses (local currency and USD where reported).
    Data collection and quality assurance was performed by national counterpart institutions
    under UNDRR coordination as part of the Sendai Framework Monitoring initiative.
    Datasets were published on the Humanitarian Data Exchange (HDX) platform by UNDRR.
  sources:
  - id: source_desinventar
    license: null
    name: DesInventar Sendai
    risk_data_type: null
    type: dataset
    url: https://www.desinventar.net/
    used_in: loss
  - id: source_hdx
    license: null
    name: Humanitarian Data Exchange (HDX)
    risk_data_type: null
    type: dataset
    url: https://data.humdata.org/dataset/d16485d0-2011-4f5d-bb12-9e92feb8f853
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/d16485d0-2011-4f5d-bb12-9e92feb8f853
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from drought (DROUGHT) events in Niger. DesInventar records: 46 events
      with data out of 289 total drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_001_drought_affected
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
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from drought
      (DROUGHT) events in Niger. DesInventar records: 15 events with data out of 289
      total drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_002_drought_damages_in_crops_ha
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: hectare
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from drought
      (DROUGHT) events in Niger. DesInventar records: 2 events with data out of 289
      total drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_003_drought_deaths
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
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from drought (DROUGHT)
      events in Niger. DesInventar records: 6 events with data out of 289 total drought
      events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_004_drought_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: XOF
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from drought (DROUGHT) events in Niger.
      DesInventar records: 14 events with data out of 289 total drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_005_drought_lost_cattle
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons permanently relocated from homes from drought (DROUGHT)
      events in Niger. DesInventar records: 10 events with data out of 289 total drought
      events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_006_drought_relocated
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
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      drought (DROUGHT) events in Niger. DesInventar records: 143 events with data
      out of 289 total drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_007_drought_victims
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
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from flood (FLOOD) events in Niger. DesInventar records: 214 events with
      data out of 763 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_008_flood_affected
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
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from flood
      (FLOOD) events in Niger. DesInventar records: 239 events with data out of 763
      total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_009_flood_damages_in_crops_ha
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: hectare
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from flood (FLOOD)
      events in Niger. DesInventar records: 49 events with data out of 763 total flood
      events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_010_flood_deaths
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed educational facilities destroyed or affected from flood
      (FLOOD) events in Niger. DesInventar records: 5 events with data out of 763
      total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_011_flood_education_centers
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed health facilities destroyed or affected from flood (FLOOD)
      events in Niger. DesInventar records: 1 events with data out of 763 total flood
      events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_012_flood_hospitals
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      flood (FLOOD) events in Niger. DesInventar records: 29 events with data out
      of 763 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_013_flood_houses_damaged
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: damage
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from flood (FLOOD)
      events in Niger. DesInventar records: 410 events with data out of 763 total
      flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_014_flood_houses_destroyed
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from flood (FLOOD) events in Niger. DesInventar records: 34 events with data
      out of 763 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_015_flood_injured
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
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from flood (FLOOD)
      events in Niger. DesInventar records: 9 events with data out of 763 total flood
      events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_016_flood_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: XOF
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in US Dollars from flood (FLOOD)
      events in Niger. DesInventar records: 1 events with data out of 763 total flood
      events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_017_flood_losses_usd
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from flood (FLOOD) events in Niger. DesInventar
      records: 122 events with data out of 763 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_018_flood_lost_cattle
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons permanently relocated from homes from flood (FLOOD)
      events in Niger. DesInventar records: 2 events with data out of 763 total flood
      events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_019_flood_relocated
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
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      flood (FLOOD) events in Niger. DesInventar records: 456 events with data out
      of 763 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_020_flood_victims
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
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from wildfire (FIRE, FOREST FIRE) events in Niger. DesInventar records:
      78 events with data out of 310 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_021_wildfire_affected
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
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from wildfire
      (FIRE, FOREST FIRE) events in Niger. DesInventar records: 168 events with data
      out of 310 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_022_wildfire_damages_in_crops_ha
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: hectare
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from wildfire
      (FIRE, FOREST FIRE) events in Niger. DesInventar records: 23 events with data
      out of 310 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_023_wildfire_deaths
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed educational facilities destroyed or affected from wildfire
      (FIRE, FOREST FIRE) events in Niger. DesInventar records: 2 events with data
      out of 310 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_024_wildfire_education_centers
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      wildfire (FIRE, FOREST FIRE) events in Niger. DesInventar records: 2 events
      with data out of 310 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_025_wildfire_houses_damaged
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: damage
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from wildfire (FIRE,
      FOREST FIRE) events in Niger. DesInventar records: 28 events with data out of
      310 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_026_wildfire_houses_destroyed
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from wildfire (FIRE,
      FOREST FIRE) events in Niger. DesInventar records: 14 events with data out of
      310 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_027_wildfire_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: XOF
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in US Dollars from wildfire (FIRE,
      FOREST FIRE) events in Niger. DesInventar records: 2 events with data out of
      310 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_028_wildfire_losses_usd
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: USD
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from wildfire (FIRE, FOREST FIRE) events
      in Niger. DesInventar records: 14 events with data out of 310 total wildfire
      events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_029_wildfire_lost_cattle
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      wildfire (FIRE, FOREST FIRE) events in Niger. DesInventar records: 48 events
      with data out of 310 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_030_wildfire_victims
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
project:
  name: DesInventar Sendai - Disaster Information Management System
  url: https://www.desinventar.net/
publisher:
  affiliation: null
  email: isdr@un.org
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://www.undrr.org/
purpose: To document historical disaster losses in Niger from the DesInventar national
  disaster loss inventory, supporting disaster risk reduction monitoring under the
  Sendai Framework.
referenced_by: []
resources:
- access_url: https://data.humdata.org/dataset/d16485d0-2011-4f5d-bb12-9e92feb8f853
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Number of Deaths, Injured, Missing, Houses Destroyed, Houses Damaged,
    Victims Affected, Relocated, Evacuated, Losses and Damages in crops by climate
    change event
  download_url: https://data.humdata.org/dataset/d16485d0-2011-4f5d-bb12-9e92feb8f853/resource/9b9d4019-129f-4df2-9499-09558b893bf8/download/niger.xlsx
  format: null
  id: resource_001
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Number of Deaths, Injured, Missing, Houses Destroyed, Houses Damaged, Victims
    Affected, Relocated, Evacuated, Losses and Damages in crops by climate change
    event
- access_url: https://data.humdata.org/dataset/d16485d0-2011-4f5d-bb12-9e92feb8f853
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DesInventar disaster loss data for Niger
  download_url: https://data.humdata.org/dataset/d16485d0-2011-4f5d-bb12-9e92feb8f853/resource/d6b6609d-3e6d-41f9-b14b-d6f4035d2d56/download/niger.zip
  format: null
  id: resource_002
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Niger.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ner_undrr_desinventar_a
spatial:
  bbox:
  - 0.15
  - 11.7
  - 15.97
  - 23.52
  centroid: null
  countries:
  - NER
  gazetteer_entries:
  - description: Niger
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/2440476/niger.html
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: DesInventar Disaster Loss and Damage Dataset for Niger
version: '1'
vulnerability: null
---
