---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Cellule de Prevention et Gestion des Urgences (CPGU)
  url: https://data.humdata.org/dataset/b2bac671-00d7-4303-8cbe-046c90b159ff
creator:
  affiliation: null
  email: isdr@un.org
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://www.desinventar.net/
dataset_id: rdls_lss-mdg_undrr_desinventar
description: 'National disaster loss inventory for Madagascar from the DesInventar
  Sendai Framework Monitor database, compiled by Cellule de Prevention et Gestion
  des Urgences (CPGU) and published by the United Nations Office for Disaster Risk
  Reduction (UNDRR). Contains 227 event-level loss records covering 2008-2015, with
  observed impacts from flood, wildfire events. Loss data includes human casualties,
  displacement, building damage, economic losses, agricultural damage, and infrastructure
  impacts. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX) at https://data.humdata.org] [Original dataset: https://data.humdata.org/dataset/b2bac671-00d7-4303-8cbe-046c90b159ff]'
details: 'Event-level disaster loss records from the DesInventar database for Madagascar,
  maintained by Cellule de Prevention et Gestion des Urgences (CPGU). Combines two
  HDX source datasets: 227 observed events from 2009 and 244 observed events from
  2008-2015. Data collected through direct observational reporting and includes human
  impacts (deaths, injuries, missing, affected, evacuated, relocated), physical impacts
  (houses destroyed/damaged), economic losses (local currency), and agricultural impacts
  (crop damage in hectares). Methodology: Direct Observational Data / Anecdotal Data.'
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
    url: https://data.humdata.org/dataset/b2bac671-00d7-4303-8cbe-046c90b159ff
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/b2bac671-00d7-4303-8cbe-046c90b159ff
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from flood (FLOOD) events in Madagascar. DesInventar records: 9 events
      with data out of 9 total flood events.'
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
      (FLOOD) events in Madagascar. DesInventar records: 4 events with data out of
      9 total flood events.'
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
      events in Madagascar. DesInventar records: 2 events with data out of 9 total
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
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from flood (FLOOD)
      events in Madagascar. DesInventar records: 4 events with data out of 9 total
      flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_004_flood_houses_destroyed
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
      flood (FLOOD) events in Madagascar. DesInventar records: 9 events with data
      out of 9 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_005_flood_victims
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
      work) from wildfire (FIRE) events in Madagascar. DesInventar records: 159 events
      with data out of 218 total wildfire events (2009-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_006_wildfire_affected
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
    description: 'Observed deaths directly caused by disaster events from wildfire
      (FIRE) events in Madagascar. DesInventar records: 14 events with data out of
      218 total wildfire events (2009-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_007_wildfire_deaths
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
      (FIRE) events in Madagascar. DesInventar records: 9 events with data out of
      218 total wildfire events (2009-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_008_wildfire_education_centers
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
      wildfire (FIRE) events in Madagascar. DesInventar records: 1 events with data
      out of 218 total wildfire events (2009-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_009_wildfire_houses_damaged
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
      events in Madagascar. DesInventar records: 198 events with data out of 218 total
      wildfire events (2009-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_010_wildfire_houses_destroyed
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
      from wildfire (FIRE) events in Madagascar. DesInventar records: 24 events with
      data out of 218 total wildfire events (2009-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_011_wildfire_injured
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
    description: 'Observed persons whose goods/services suffered serious damage from
      wildfire (FIRE) events in Madagascar. DesInventar records: 136 events with data
      out of 218 total wildfire events (2009-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_012_wildfire_victims
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
    description: 'Observed deaths directly caused by disaster events from drought
      (DROUGHT) events in Madagascar. DesInventar records: 3 events with data out
      of 3 total drought events (2015-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_013_drought_deaths
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
      work) from flood (FLOOD) events in Madagascar. DesInventar records: 19 events
      with data out of 20 total flood events (2008-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_014_flood_affected
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
      (FLOOD) events in Madagascar. DesInventar records: 9 events with data out of
      20 total flood events (2008-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_015_flood_damages_in_crops_ha
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
      events in Madagascar. DesInventar records: 8 events with data out of 20 total
      flood events (2008-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_016_flood_deaths
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
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from flood (FLOOD)
      events in Madagascar. DesInventar records: 10 events with data out of 20 total
      flood events (2008-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_017_flood_houses_destroyed
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
      events in Madagascar. DesInventar records: 7 events with data out of 20 total
      flood events (2008-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_018_flood_relocated
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
      flood (FLOOD) events in Madagascar. DesInventar records: 19 events with data
      out of 20 total flood events (2008-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_019_flood_victims
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
    description: 'Observed deaths directly caused by disaster events from landslide
      (LANDSLIDE) events in Madagascar. DesInventar records: 2 events with data out
      of 2 total landslide events (2015-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_020_landslide_deaths
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
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from landslide (LANDSLIDE)
      events in Madagascar. DesInventar records: 2 events with data out of 2 total
      landslide events (2015-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_021_landslide_houses_destroyed
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
      landslide (LANDSLIDE) events in Madagascar. DesInventar records: 1 events with
      data out of 2 total landslide events (2015-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_022_landslide_victims
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
      work) from wildfire (FIRE) events in Madagascar. DesInventar records: 159 events
      with data out of 219 total wildfire events (2009-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_023_wildfire_affected
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
    description: 'Observed deaths directly caused by disaster events from wildfire
      (FIRE) events in Madagascar. DesInventar records: 14 events with data out of
      219 total wildfire events (2009-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_024_wildfire_deaths
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
      (FIRE) events in Madagascar. DesInventar records: 9 events with data out of
      219 total wildfire events (2009-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_025_wildfire_education_centers
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
      wildfire (FIRE) events in Madagascar. DesInventar records: 1 events with data
      out of 219 total wildfire events (2009-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_026_wildfire_houses_damaged
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
      events in Madagascar. DesInventar records: 199 events with data out of 219 total
      wildfire events (2009-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_027_wildfire_houses_destroyed
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
      from wildfire (FIRE) events in Madagascar. DesInventar records: 24 events with
      data out of 219 total wildfire events (2009-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_028_wildfire_injured
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
    description: 'Observed persons whose goods/services suffered serious damage from
      wildfire (FIRE) events in Madagascar. DesInventar records: 137 events with data
      out of 219 total wildfire events (2009-2015).'
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
purpose: To document historical disaster losses in Madagascar from the DesInventar
  national disaster loss inventory, supporting disaster risk reduction monitoring
  under the Sendai Framework.
referenced_by: []
resources:
- access_url: https://data.humdata.org/dataset/b2bac671-00d7-4303-8cbe-046c90b159ff
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Number of Deaths, Injured, Missing, Houses Destroyed, Houses Damaged,
    Victims Affected, Relocated, Evacuated, Losses and Damages in crops by climate
    change event
  download_url: https://data.humdata.org/dataset/b2bac671-00d7-4303-8cbe-046c90b159ff/resource/7775fc9a-2f75-4015-85e7-1d5943a9d2ce/download/madagascar.xlsx
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
- access_url: https://data.humdata.org/dataset/b2bac671-00d7-4303-8cbe-046c90b159ff
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DesInventar disaster loss data for Madagascar
  download_url: https://data.humdata.org/dataset/b2bac671-00d7-4303-8cbe-046c90b159ff/resource/0090e8a4-8500-44e9-9ca8-659cf30ea97b/download/madagascar.zip
  format: null
  id: resource_002
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Madagascar.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mdg_undrr_desinventar
spatial:
  bbox:
  - 43.22
  - -25.6
  - 50.5
  - -11.94
  centroid: null
  countries:
  - MDG
  gazetteer_entries:
  - description: Madagascar
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/1062947/madagascar.html
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: DesInventar Disaster Loss and Damage Dataset for Madagascar
version: '1'
vulnerability: null
---
