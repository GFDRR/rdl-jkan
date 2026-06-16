---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Direction de la Protection Civile (DPC)
  url: https://data.humdata.org/dataset/dc29e362-55fc-458f-af09-477d3f0e2bcb
creator:
  affiliation: null
  email: isdr@un.org
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://www.desinventar.net/
dataset_id: rdls_lss-sen_undrr_desinventar_a
description: 'National disaster loss inventory for Senegal from the DesInventar Sendai
  Framework Monitor database, compiled by Direction de la Protection Civile (DPC)
  and published by the United Nations Office for Disaster Risk Reduction (UNDRR).
  Contains 778 event-level loss records covering 1984-1992, with observed impacts
  from drought, flood, strong_wind, wildfire events. Loss data includes human casualties,
  displacement, building damage, economic losses, agricultural damage, and infrastructure
  impacts. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX) at https://data.humdata.org] [Original dataset: https://data.humdata.org/dataset/dc29e362-55fc-458f-af09-477d3f0e2bcb]'
details: 'Event-level disaster loss records from the DesInventar database for Senegal,
  maintained by Direction de la Protection Civile (DPC). Covers 778 observed disaster
  events from 1984-1992. Data collected through direct observational reporting and
  includes human impacts (deaths, injuries, missing, affected, evacuated, relocated),
  physical impacts (houses destroyed/damaged, education centres, hospitals, roads),
  economic losses (local currency and USD), and agricultural impacts (crop damage
  in hectares, livestock losses). Methodology: Direct Observational Data / Anecdotal
  Data.'
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
    url: https://data.humdata.org/dataset/dc29e362-55fc-458f-af09-477d3f0e2bcb
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/dc29e362-55fc-458f-af09-477d3f0e2bcb
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from flood (FLOOD) events in Senegal. DesInventar records: 18 events with
      data out of 149 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_001_flood_affected
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
      (FLOOD) events in Senegal. DesInventar records: 14 events with data out of 149
      total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_002_flood_damages_in_crops_ha
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
      events in Senegal. DesInventar records: 22 events with data out of 149 total
      flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_003_flood_deaths
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
      (FLOOD) events in Senegal. DesInventar records: 2 events with data out of 149
      total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_004_flood_education_centers
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
    description: 'Observed persons temporarily evacuated from homes or workplaces
      from flood (FLOOD) events in Senegal. DesInventar records: 2 events with data
      out of 149 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_005_flood_evacuated
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed health facilities destroyed or affected from flood (FLOOD)
      events in Senegal. DesInventar records: 2 events with data out of 149 total
      flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_006_flood_hospitals
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
      flood (FLOOD) events in Senegal. DesInventar records: 45 events with data out
      of 149 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_007_flood_houses_damaged
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
      events in Senegal. DesInventar records: 8 events with data out of 149 total
      flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_008_flood_houses_destroyed
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
      from flood (FLOOD) events in Senegal. DesInventar records: 12 events with data
      out of 149 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_009_flood_injured
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
      events in Senegal. DesInventar records: 3 events with data out of 149 total
      flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_010_flood_losses_local
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
      events in Senegal. DesInventar records: 2 events with data out of 149 total
      flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_011_flood_losses_usd
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
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons missing or unaccounted for after disaster events
      from flood (FLOOD) events in Senegal. DesInventar records: 4 events with data
      out of 149 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_012_flood_missing
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
    description: 'Observed persons permanently relocated from homes from flood (FLOOD)
      events in Senegal. DesInventar records: 3 events with data out of 149 total
      flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_013_flood_relocated
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
      flood (FLOOD) events in Senegal. DesInventar records: 16 events with data out
      of 149 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_014_flood_victims
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
    description: 'Observed deaths directly caused by disaster events from strong wind
      (STORM) events in Senegal. DesInventar records: 2 events with data out of 13
      total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_015_strongwind_deaths
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
    description: 'Observed persons temporarily evacuated from homes or workplaces
      from strong wind (STORM) events in Senegal. DesInventar records: 7 events with
      data out of 13 total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_016_strongwind_evacuated
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
    description: 'Observed persons missing or unaccounted for after disaster events
      from strong wind (STORM) events in Senegal. DesInventar records: 11 events with
      data out of 13 total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_017_strongwind_missing
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
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from wildfire (FIRE) events in Senegal. DesInventar records: 4 events
      with data out of 580 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_018_wildfire_affected
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
      (FIRE) events in Senegal. DesInventar records: 1 events with data out of 580
      total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_019_wildfire_damages_in_crops_ha
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
      (FIRE) events in Senegal. DesInventar records: 50 events with data out of 580
      total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_020_wildfire_deaths
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
      (FIRE) events in Senegal. DesInventar records: 17 events with data out of 580
      total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_021_wildfire_education_centers
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
    description: 'Observed health facilities destroyed or affected from wildfire (FIRE)
      events in Senegal. DesInventar records: 3 events with data out of 580 total
      wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_022_wildfire_hospitals
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
      wildfire (FIRE) events in Senegal. DesInventar records: 204 events with data
      out of 580 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_023_wildfire_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from wildfire (FIRE)
      events in Senegal. DesInventar records: 16 events with data out of 580 total
      wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_024_wildfire_houses_destroyed
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
      from wildfire (FIRE) events in Senegal. DesInventar records: 29 events with
      data out of 580 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_025_wildfire_injured
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
    description: 'Observed total economic losses in local currency from wildfire (FIRE)
      events in Senegal. DesInventar records: 2 events with data out of 580 total
      wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_026_wildfire_losses_local
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
    description: 'Observed total economic losses in US Dollars from wildfire (FIRE)
      events in Senegal. DesInventar records: 59 events with data out of 580 total
      wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_027_wildfire_losses_usd
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
    description: 'Observed livestock lost from wildfire (FIRE) events in Senegal.
      DesInventar records: 5 events with data out of 580 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_028_wildfire_lost_cattle
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
      wildfire (FIRE) events in Senegal. DesInventar records: 25 events with data
      out of 580 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_029_wildfire_victims
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
purpose: To document historical disaster losses in Senegal from the DesInventar national
  disaster loss inventory, supporting disaster risk reduction monitoring under the
  Sendai Framework.
referenced_by: []
resources:
- access_url: https://data.humdata.org/dataset/dc29e362-55fc-458f-af09-477d3f0e2bcb
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Number of Deaths, Injured, Missing, Houses Destroyed, Houses Damaged,
    Victims Affected, Relocated, Evacuated, Losses and Damages in crops by climate
    change event
  download_url: https://data.humdata.org/dataset/dc29e362-55fc-458f-af09-477d3f0e2bcb/resource/a93d352d-bd3f-4161-a471-8f015b89679b/download/senegal.xlsx
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
- access_url: https://data.humdata.org/dataset/dc29e362-55fc-458f-af09-477d3f0e2bcb
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DesInventar disaster loss data for Senegal
  download_url: https://data.humdata.org/dataset/dc29e362-55fc-458f-af09-477d3f0e2bcb/resource/688b6947-c44d-40bb-a9b0-46b4c5ae91d7/download/senegal.zip
  format: null
  id: resource_002
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Senegal.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sen_undrr_desinventar_a
spatial:
  bbox:
  - -17.54
  - 12.31
  - -11.38
  - 16.69
  centroid: null
  countries:
  - SEN
  gazetteer_entries:
  - description: Senegal
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/2245662/senegal.html
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: DesInventar Disaster Loss and Damage Dataset for Senegal
version: '1'
vulnerability: null
---
