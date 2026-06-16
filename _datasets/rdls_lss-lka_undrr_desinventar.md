---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Disaster Management Centre (DMC)
  url: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184
creator:
  affiliation: null
  email: isdr@un.org
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://www.desinventar.net/
dataset_id: rdls_lss-lka_undrr_desinventar
description: 'National disaster loss inventory for Sri Lanka from the DesInventar
  Sendai Framework Monitor database, compiled by Disaster Management Centre (DMC)
  and published by the United Nations Office for Disaster Risk Reduction (UNDRR).
  Contains 17,729 event-level loss records covering historical, with observed impacts
  from coastal_flood, convective_storm, drought, extreme_temperature, flood, landslide,
  strong_wind, tsunami, wildfire events. Loss data includes human casualties, displacement,
  building damage, economic losses, agricultural damage, and infrastructure impacts.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX) at https://data.humdata.org] [Original dataset: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184]'
details: 'Event-level disaster loss records from the DesInventar database for Sri
  Lanka, maintained by Disaster Management Centre (DMC). Covers 17,729 observed disaster
  events from historical. Data collected through direct observational reporting and
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
    url: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from coastal flood (SURGE, TIDAL WAVE) events in Sri Lanka. DesInventar
      records: 20 events with data out of 40 total coastal flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_001_coastalflood_affected
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
    description: 'Observed deaths directly caused by disaster events from coastal
      flood (SURGE, TIDAL WAVE) events in Sri Lanka. DesInventar records: 4 events
      with data out of 40 total coastal flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_002_coastalflood_deaths
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
      from coastal flood (SURGE, TIDAL WAVE) events in Sri Lanka. DesInventar records:
      1 events with data out of 40 total coastal flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_003_coastalflood_evacuated
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
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      coastal flood (SURGE, TIDAL WAVE) events in Sri Lanka. DesInventar records:
      7 events with data out of 40 total coastal flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_004_coastalflood_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from coastal flood
      (SURGE, TIDAL WAVE) events in Sri Lanka. DesInventar records: 2 events with
      data out of 40 total coastal flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_005_coastalflood_houses_destroyed
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
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from convective storm (HAILSTORM) events in Sri Lanka. DesInventar records:
      1 events with data out of 20 total convective storm events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_006_convectivestorm_affected
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
    description: 'Observed deaths directly caused by disaster events from convective
      storm (HAILSTORM) events in Sri Lanka. DesInventar records: 1 events with data
      out of 20 total convective storm events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_007_convectivestorm_deaths
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
    description: 'Observed homes with non-structural damage, still habitable from
      convective storm (HAILSTORM) events in Sri Lanka. DesInventar records: 1 events
      with data out of 20 total convective storm events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_008_convectivestorm_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from convective storm
      (HAILSTORM) events in Sri Lanka. DesInventar records: 1 events with data out
      of 20 total convective storm events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_009_convectivestorm_houses_destroyed
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
      from convective storm (HAILSTORM) events in Sri Lanka. DesInventar records:
      1 events with data out of 20 total convective storm events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_010_convectivestorm_injured
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
      work) from drought (DROUGHT) events in Sri Lanka. DesInventar records: 1,327
      events with data out of 2,242 total drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_011_drought_affected
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
      (DROUGHT) events in Sri Lanka. DesInventar records: 97 events with data out
      of 2,242 total drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_012_drought_damages_in_crops_ha
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
      (DROUGHT) events in Sri Lanka. DesInventar records: 1 events with data out of
      2,242 total drought events.'
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
    description: 'Observed persons temporarily evacuated from homes or workplaces
      from drought (DROUGHT) events in Sri Lanka. DesInventar records: 1 events with
      data out of 2,242 total drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_014_drought_evacuated
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
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      drought (DROUGHT) events in Sri Lanka. DesInventar records: 3 events with data
      out of 2,242 total drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_015_drought_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from drought (DROUGHT)
      events in Sri Lanka. DesInventar records: 1 events with data out of 2,242 total
      drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_016_drought_houses_destroyed
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
    description: 'Observed persons missing or unaccounted for after disaster events
      from drought (DROUGHT) events in Sri Lanka. DesInventar records: 1 events with
      data out of 2,242 total drought events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_017_drought_missing
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
      work) from flood (FLASH FLOOD, FLOOD) events in Sri Lanka. DesInventar records:
      5,541 events with data out of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_018_flood_affected
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
      (FLASH FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 5 events with
      data out of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_019_flood_damages_in_crops_ha
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
    description: 'Observed deaths directly caused by disaster events from flood (FLASH
      FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 252 events with data
      out of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_020_flood_deaths
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
      (FLASH FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 2 events with
      data out of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_021_flood_education_centers
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
      from flood (FLASH FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 82
      events with data out of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_022_flood_evacuated
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
    description: 'Observed health facilities destroyed or affected from flood (FLASH
      FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 1 events with data out
      of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_023_flood_hospitals
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
      flood (FLASH FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 2,297 events
      with data out of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_024_flood_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from flood (FLASH FLOOD,
      FLOOD) events in Sri Lanka. DesInventar records: 1,229 events with data out
      of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_025_flood_houses_destroyed
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
      from flood (FLASH FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 80
      events with data out of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_026_flood_injured
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
    description: 'Observed total economic losses in local currency from flood (FLASH
      FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 7 events with data out
      of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_027_flood_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: LKR
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons missing or unaccounted for after disaster events
      from flood (FLASH FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 10
      events with data out of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_028_flood_missing
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
    description: 'Observed persons permanently relocated from homes from flood (FLASH
      FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 5 events with data out
      of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_029_flood_relocated
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
      flood (FLASH FLOOD, FLOOD) events in Sri Lanka. DesInventar records: 2 events
      with data out of 6,828 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_030_flood_victims
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
      work) from flood (RAINS) events in Sri Lanka. DesInventar records: 2,405 events
      with data out of 2,533 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_031_flood_affected
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
    description: 'Observed deaths directly caused by disaster events from flood (RAINS)
      events in Sri Lanka. DesInventar records: 23 events with data out of 2,533 total
      flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_032_flood_deaths
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
      from flood (RAINS) events in Sri Lanka. DesInventar records: 19 events with
      data out of 2,533 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_033_flood_evacuated
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
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      flood (RAINS) events in Sri Lanka. DesInventar records: 1,829 events with data
      out of 2,533 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_034_flood_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from flood (RAINS)
      events in Sri Lanka. DesInventar records: 198 events with data out of 2,533
      total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_035_flood_houses_destroyed
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
      from flood (RAINS) events in Sri Lanka. DesInventar records: 17 events with
      data out of 2,533 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_036_flood_injured
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
    description: 'Observed persons missing or unaccounted for after disaster events
      from flood (RAINS) events in Sri Lanka. DesInventar records: 1 events with data
      out of 2,533 total flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_037_flood_missing
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
    description: 'Observed persons permanently relocated from homes from flood (RAINS)
      events in Sri Lanka. DesInventar records: 1 events with data out of 2,533 total
      flood events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_038_flood_relocated
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
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from landslide (LANDSLIDE) events in Sri Lanka. DesInventar records: 1,545
      events with data out of 2,100 total landslide events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_039_landslide_affected
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
      (LANDSLIDE) events in Sri Lanka. DesInventar records: 174 events with data out
      of 2,100 total landslide events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_040_landslide_deaths
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
      from landslide (LANDSLIDE) events in Sri Lanka. DesInventar records: 46 events
      with data out of 2,100 total landslide events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_041_landslide_evacuated
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
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      landslide (LANDSLIDE) events in Sri Lanka. DesInventar records: 1,067 events
      with data out of 2,100 total landslide events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_042_landslide_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from landslide (LANDSLIDE)
      events in Sri Lanka. DesInventar records: 316 events with data out of 2,100
      total landslide events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_043_landslide_houses_destroyed
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
      from landslide (LANDSLIDE) events in Sri Lanka. DesInventar records: 125 events
      with data out of 2,100 total landslide events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_044_landslide_injured
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
    description: 'Observed total economic losses in local currency from landslide
      (LANDSLIDE) events in Sri Lanka. DesInventar records: 4 events with data out
      of 2,100 total landslide events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_045_landslide_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: LKR
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons missing or unaccounted for after disaster events
      from landslide (LANDSLIDE) events in Sri Lanka. DesInventar records: 4 events
      with data out of 2,100 total landslide events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_046_landslide_missing
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
    description: 'Observed persons permanently relocated from homes from landslide
      (LANDSLIDE) events in Sri Lanka. DesInventar records: 8 events with data out
      of 2,100 total landslide events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_047_landslide_relocated
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
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from strong wind (STORM) events in Sri Lanka. DesInventar records: 2 events
      with data out of 4 total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_048_strongwind_affected
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
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      strong wind (STORM) events in Sri Lanka. DesInventar records: 2 events with
      data out of 4 total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_049_strongwind_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from strong wind (STORM)
      events in Sri Lanka. DesInventar records: 2 events with data out of 4 total
      strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_050_strongwind_houses_destroyed
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
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from strong wind (CYCLONE) events in Sri Lanka. DesInventar records: 117
      events with data out of 164 total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_051_strongwind_affected
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
      (CYCLONE) events in Sri Lanka. DesInventar records: 27 events with data out
      of 164 total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_052_strongwind_deaths
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
      from strong wind (CYCLONE) events in Sri Lanka. DesInventar records: 4 events
      with data out of 164 total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_053_strongwind_evacuated
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
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      strong wind (CYCLONE) events in Sri Lanka. DesInventar records: 106 events with
      data out of 164 total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_054_strongwind_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from strong wind (CYCLONE)
      events in Sri Lanka. DesInventar records: 36 events with data out of 164 total
      strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_055_strongwind_houses_destroyed
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
      from strong wind (CYCLONE) events in Sri Lanka. DesInventar records: 16 events
      with data out of 164 total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_056_strongwind_injured
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
    description: 'Observed persons missing or unaccounted for after disaster events
      from strong wind (CYCLONE) events in Sri Lanka. DesInventar records: 2 events
      with data out of 164 total strong wind events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_057_strongwind_missing
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
      work) from tsunami (TSUNAMI) events in Sri Lanka. DesInventar records: 69 events
      with data out of 89 total tsunami events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_058_tsunami_affected
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
    description: 'Observed deaths directly caused by disaster events from tsunami
      (TSUNAMI) events in Sri Lanka. DesInventar records: 13 events with data out
      of 89 total tsunami events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_059_tsunami_deaths
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
    description: 'Observed homes with non-structural damage, still habitable from
      tsunami (TSUNAMI) events in Sri Lanka. DesInventar records: 57 events with data
      out of 89 total tsunami events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_060_tsunami_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from tsunami (TSUNAMI)
      events in Sri Lanka. DesInventar records: 57 events with data out of 89 total
      tsunami events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_061_tsunami_houses_destroyed
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
      from tsunami (TSUNAMI) events in Sri Lanka. DesInventar records: 40 events with
      data out of 89 total tsunami events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_062_tsunami_injured
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
    description: 'Observed total economic losses in local currency from tsunami (TSUNAMI)
      events in Sri Lanka. DesInventar records: 3 events with data out of 89 total
      tsunami events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_063_tsunami_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: LKR
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons missing or unaccounted for after disaster events
      from tsunami (TSUNAMI) events in Sri Lanka. DesInventar records: 35 events with
      data out of 89 total tsunami events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_064_tsunami_missing
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
      work) from wildfire (FIRE, FOREST FIRE) events in Sri Lanka. DesInventar records:
      983 events with data out of 3,697 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_065_wildfire_affected
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
      (FIRE, FOREST FIRE) events in Sri Lanka. DesInventar records: 61 events with
      data out of 3,697 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_066_wildfire_deaths
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
      from wildfire (FIRE, FOREST FIRE) events in Sri Lanka. DesInventar records:
      16 events with data out of 3,697 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_067_wildfire_evacuated
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
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      wildfire (FIRE, FOREST FIRE) events in Sri Lanka. DesInventar records: 423 events
      with data out of 3,697 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_068_wildfire_houses_damaged
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
      FOREST FIRE) events in Sri Lanka. DesInventar records: 538 events with data
      out of 3,697 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_069_wildfire_houses_destroyed
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
      from wildfire (FIRE, FOREST FIRE) events in Sri Lanka. DesInventar records:
      36 events with data out of 3,697 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_070_wildfire_injured
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
    description: 'Observed total economic losses in local currency from wildfire (FIRE,
      FOREST FIRE) events in Sri Lanka. DesInventar records: 3 events with data out
      of 3,697 total wildfire events.'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_071_wildfire_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: LKR
        metric: loss
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
purpose: To document historical disaster losses in Sri Lanka from the DesInventar
  national disaster loss inventory, supporting disaster risk reduction monitoring
  under the Sendai Framework.
referenced_by: []
resources:
- access_url: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DesInventar Disaster Loss and Damage Dataset for Sri Lanka (Disaster
    data for Sri Lanka)
  download_url: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184/resource/49adba32-509f-49e7-b63e-928ef743c52e/download/srilanka.zip
  format: null
  id: resource_001
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Disaster data for Sri Lanka
- access_url: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DesInventar Disaster Loss and Damage Dataset for Sri Lanka (Disaster
    tabular data for Sri Lanka)
  download_url: https://data.humdata.org/dataset/08c9ca36-8b95-4361-abf1-ce21bfc49184/resource/4cb4bd14-e5ba-4443-af23-948bfb05f479/download/di_report-srilanka.xls
  format: null
  id: resource_002
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Disaster tabular data for Sri Lanka
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lka_undrr_desinventar
spatial:
  bbox:
  - 79.66
  - 5.92
  - 81.89
  - 9.83
  centroid: null
  countries:
  - LKA
  gazetteer_entries:
  - description: Sri Lanka
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/1227603/sri-lanka.html
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: DesInventar Disaster Loss and Damage Dataset for Sri Lanka
version: '1'
vulnerability: null
---
