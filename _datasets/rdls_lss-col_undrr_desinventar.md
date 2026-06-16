---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Corporacion OSSO / La Red
  url: https://data.humdata.org/dataset/baeedcfd-14c7-4028-8eb0-e1192e82dc79
creator:
  affiliation: null
  email: isdr@un.org
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://www.desinventar.net/
dataset_id: rdls_lss-col_undrr_desinventar
description: 'National disaster loss inventory for Colombia from the DesInventar Sendai
  Framework Monitor database, compiled by Corporacion OSSO / La Red and published
  by the United Nations Office for Disaster Risk Reduction (UNDRR). Contains 28,916
  event-level loss records covering 1963-2013, with observed impacts from coastal_flood,
  convective_storm, drought, earthquake, extreme_temperature, flood, landslide, strong_wind,
  tsunami, wildfire events. Loss data includes human casualties, displacement, building
  damage, economic losses, agricultural damage, and infrastructure impacts. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX) at https://data.humdata.org] [Original dataset: https://data.humdata.org/dataset/baeedcfd-14c7-4028-8eb0-e1192e82dc79]'
details: 'Event-level disaster loss records from the DesInventar database for Colombia,
  maintained by Corporacion OSSO / La Red. Covers 28,916 observed disaster events
  from 1963-2013. Data collected through direct observational reporting and includes
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
    url: https://data.humdata.org/dataset/baeedcfd-14c7-4028-8eb0-e1192e82dc79
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/baeedcfd-14c7-4028-8eb0-e1192e82dc79
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from coastal flood (SURGE) events in Colombia. DesInventar records: 52
      events with data out of 159 total coastal flood events (1984-2013).'
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
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from coastal
      flood (SURGE) events in Colombia. DesInventar records: 1 events with data out
      of 159 total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_002_coastalflood_damages_in_crops_ha
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from coastal flood
      (SURGE) events in Colombia. DesInventar records: 2 events with data out of 159
      total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_003_coastalflood_damages_in_roads_mts
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
    description: 'Observed deaths directly caused by disaster events from coastal
      flood (SURGE) events in Colombia. DesInventar records: 18 events with data out
      of 159 total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_004_coastalflood_deaths
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
    description: 'Observed educational facilities destroyed or affected from coastal
      flood (SURGE) events in Colombia. DesInventar records: 2 events with data out
      of 159 total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_005_coastalflood_education_centers
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
      from coastal flood (SURGE) events in Colombia. DesInventar records: 8 events
      with data out of 159 total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_006_coastalflood_evacuated
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
    description: 'Observed health facilities destroyed or affected from coastal flood
      (SURGE) events in Colombia. DesInventar records: 1 events with data out of 159
      total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_007_coastalflood_hospitals
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
      coastal flood (SURGE) events in Colombia. DesInventar records: 33 events with
      data out of 159 total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_008_coastalflood_houses_damaged
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
      (SURGE) events in Colombia. DesInventar records: 52 events with data out of
      159 total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_009_coastalflood_houses_destroyed
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
      from coastal flood (SURGE) events in Colombia. DesInventar records: 4 events
      with data out of 159 total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_010_coastalflood_injured
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
    description: 'Observed total economic losses in local currency from coastal flood
      (SURGE) events in Colombia. DesInventar records: 8 events with data out of 159
      total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_011_coastalflood_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: COP
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons missing or unaccounted for after disaster events
      from coastal flood (SURGE) events in Colombia. DesInventar records: 9 events
      with data out of 159 total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_012_coastalflood_missing
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
      coastal flood (SURGE) events in Colombia. DesInventar records: 12 events with
      data out of 159 total coastal flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_013_coastalflood_victims
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
      work) from convective storm (HAILSTORM) events in Colombia. DesInventar records:
      39 events with data out of 81 total convective storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_014_convectivestorm_affected
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
    description: 'Observed hectares of crops/woods destroyed or affected from convective
      storm (HAILSTORM) events in Colombia. DesInventar records: 6 events with data
      out of 81 total convective storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_015_convectivestorm_damages_in_crops_ha
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from convective
      storm (HAILSTORM) events in Colombia. DesInventar records: 1 events with data
      out of 81 total convective storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_016_convectivestorm_damages_in_roads_mts
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
    description: 'Observed educational facilities destroyed or affected from convective
      storm (HAILSTORM) events in Colombia. DesInventar records: 4 events with data
      out of 81 total convective storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_017_convectivestorm_education_centers
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
    description: 'Observed health facilities destroyed or affected from convective
      storm (HAILSTORM) events in Colombia. DesInventar records: 2 events with data
      out of 81 total convective storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_018_convectivestorm_hospitals
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
      convective storm (HAILSTORM) events in Colombia. DesInventar records: 30 events
      with data out of 81 total convective storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_019_convectivestorm_houses_damaged
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
      (HAILSTORM) events in Colombia. DesInventar records: 6 events with data out
      of 81 total convective storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_020_convectivestorm_houses_destroyed
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
      from convective storm (HAILSTORM) events in Colombia. DesInventar records: 2
      events with data out of 81 total convective storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_021_convectivestorm_injured
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
    description: 'Observed total economic losses in local currency from convective
      storm (HAILSTORM) events in Colombia. DesInventar records: 11 events with data
      out of 81 total convective storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_022_convectivestorm_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: COP
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from convective storm (HAILSTORM) events
      in Colombia. DesInventar records: 1 events with data out of 81 total convective
      storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_023_convectivestorm_lost_cattle
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
      convective storm (HAILSTORM) events in Colombia. DesInventar records: 4 events
      with data out of 81 total convective storm events (1989-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_024_convectivestorm_victims
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
      work) from drought (DROUGHT) events in Colombia. DesInventar records: 115 events
      with data out of 591 total drought events (1985-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_025_drought_affected
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
      (DROUGHT) events in Colombia. DesInventar records: 25 events with data out of
      591 total drought events (1985-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_026_drought_damages_in_crops_ha
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed educational facilities destroyed or affected from drought
      (DROUGHT) events in Colombia. DesInventar records: 1 events with data out of
      591 total drought events (1985-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_027_drought_education_centers
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
    description: 'Observed health facilities destroyed or affected from drought (DROUGHT)
      events in Colombia. DesInventar records: 1 events with data out of 591 total
      drought events (1985-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_028_drought_hospitals
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
      drought (DROUGHT) events in Colombia. DesInventar records: 2 events with data
      out of 591 total drought events (1985-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_029_drought_houses_damaged
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
    asset_dimension: content
    description: 'Observed total economic losses in local currency from drought (DROUGHT)
      events in Colombia. DesInventar records: 25 events with data out of 591 total
      drought events (1985-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_030_drought_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: COP
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from drought (DROUGHT) events in Colombia.
      DesInventar records: 6 events with data out of 591 total drought events (1985-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_031_drought_lost_cattle
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
      drought (DROUGHT) events in Colombia. DesInventar records: 1 events with data
      out of 591 total drought events (1985-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_032_drought_victims
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
      work) from earthquake (EARTHQUAKE) events in Colombia. DesInventar records:
      211 events with data out of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_033_earthquake_affected
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
    description: 'Observed hectares of crops/woods destroyed or affected from earthquake
      (EARTHQUAKE) events in Colombia. DesInventar records: 1 events with data out
      of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_034_earthquake_damages_in_crops_ha
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from earthquake
      (EARTHQUAKE) events in Colombia. DesInventar records: 19 events with data out
      of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_035_earthquake_damages_in_roads_mts
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
    description: 'Observed deaths directly caused by disaster events from earthquake
      (EARTHQUAKE) events in Colombia. DesInventar records: 144 events with data out
      of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_036_earthquake_deaths
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
    description: 'Observed educational facilities destroyed or affected from earthquake
      (EARTHQUAKE) events in Colombia. DesInventar records: 146 events with data out
      of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_037_earthquake_education_centers
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
      from earthquake (EARTHQUAKE) events in Colombia. DesInventar records: 11 events
      with data out of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_038_earthquake_evacuated
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
    description: 'Observed health facilities destroyed or affected from earthquake
      (EARTHQUAKE) events in Colombia. DesInventar records: 46 events with data out
      of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_039_earthquake_hospitals
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
      earthquake (EARTHQUAKE) events in Colombia. DesInventar records: 362 events
      with data out of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_040_earthquake_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from earthquake (EARTHQUAKE)
      events in Colombia. DesInventar records: 359 events with data out of 888 total
      earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_041_earthquake_houses_destroyed
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
      from earthquake (EARTHQUAKE) events in Colombia. DesInventar records: 158 events
      with data out of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_042_earthquake_injured
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
    description: 'Observed total economic losses in local currency from earthquake
      (EARTHQUAKE) events in Colombia. DesInventar records: 23 events with data out
      of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_043_earthquake_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: COP
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in US Dollars from earthquake (EARTHQUAKE)
      events in Colombia. DesInventar records: 2 events with data out of 888 total
      earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_044_earthquake_losses_usd
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
      from earthquake (EARTHQUAKE) events in Colombia. DesInventar records: 22 events
      with data out of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_045_earthquake_missing
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
      earthquake (EARTHQUAKE) events in Colombia. DesInventar records: 195 events
      with data out of 888 total earthquake events (1986-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_046_earthquake_victims
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
      work) from extreme temperature (FROST) events in Colombia. DesInventar records:
      6 events with data out of 62 total extreme temperature events (1985-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_047_extremetemperature_affected
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
    description: 'Observed hectares of crops/woods destroyed or affected from extreme
      temperature (FROST) events in Colombia. DesInventar records: 20 events with
      data out of 62 total extreme temperature events (1985-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_048_extremetemperature_damages_in_crops_ha
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
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from extreme temperature
      (FROST) events in Colombia. DesInventar records: 7 events with data out of 62
      total extreme temperature events (1985-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_049_extremetemperature_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: COP
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from extreme temperature (FROST) events
      in Colombia. DesInventar records: 1 events with data out of 62 total extreme
      temperature events (1985-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_050_extremetemperature_lost_cattle
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
      extreme temperature (FROST) events in Colombia. DesInventar records: 2 events
      with data out of 62 total extreme temperature events (1985-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_extreme_temperature
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_051_extremetemperature_victims
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
      work) from flood (FLOOD) events in Colombia. DesInventar records: 8,904 events
      with data out of 15,109 total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_052_flood_affected
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
      (FLOOD) events in Colombia. DesInventar records: 1,015 events with data out
      of 15,109 total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_053_flood_damages_in_crops_ha
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from flood (FLOOD)
      events in Colombia. DesInventar records: 484 events with data out of 15,109
      total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_054_flood_damages_in_roads_mts
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
    description: 'Observed deaths directly caused by disaster events from flood (FLOOD)
      events in Colombia. DesInventar records: 756 events with data out of 15,109
      total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_055_flood_deaths
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
      (FLOOD) events in Colombia. DesInventar records: 455 events with data out of
      15,109 total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_056_flood_education_centers
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
      from flood (FLOOD) events in Colombia. DesInventar records: 423 events with
      data out of 15,109 total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_057_flood_evacuated
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
      events in Colombia. DesInventar records: 88 events with data out of 15,109 total
      flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_058_flood_hospitals
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
      flood (FLOOD) events in Colombia. DesInventar records: 5,361 events with data
      out of 15,109 total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_059_flood_houses_damaged
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
      events in Colombia. DesInventar records: 2,279 events with data out of 15,109
      total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_060_flood_houses_destroyed
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
      from flood (FLOOD) events in Colombia. DesInventar records: 237 events with
      data out of 15,109 total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_061_flood_injured
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
      events in Colombia. DesInventar records: 958 events with data out of 15,109
      total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_062_flood_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: COP
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in US Dollars from flood (FLOOD)
      events in Colombia. DesInventar records: 1 events with data out of 15,109 total
      flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_063_flood_losses_usd
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
    description: 'Observed livestock lost from flood (FLOOD) events in Colombia. DesInventar
      records: 27 events with data out of 15,109 total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_064_flood_lost_cattle
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
      from flood (FLOOD) events in Colombia. DesInventar records: 199 events with
      data out of 15,109 total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_065_flood_missing
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
      events in Colombia. DesInventar records: 23 events with data out of 15,109 total
      flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_066_flood_relocated
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
      flood (FLOOD) events in Colombia. DesInventar records: 1,131 events with data
      out of 15,109 total flood events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_067_flood_victims
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
      work) from landslide (LANDSLIDE) events in Colombia. DesInventar records: 3,212
      events with data out of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_068_landslide_affected
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
    description: 'Observed hectares of crops/woods destroyed or affected from landslide
      (LANDSLIDE) events in Colombia. DesInventar records: 212 events with data out
      of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_069_landslide_damages_in_crops_ha
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from landslide (LANDSLIDE)
      events in Colombia. DesInventar records: 747 events with data out of 9,041 total
      landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_070_landslide_damages_in_roads_mts
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
    description: 'Observed deaths directly caused by disaster events from landslide
      (LANDSLIDE) events in Colombia. DesInventar records: 1,409 events with data
      out of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_071_landslide_deaths
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
    description: 'Observed educational facilities destroyed or affected from landslide
      (LANDSLIDE) events in Colombia. DesInventar records: 262 events with data out
      of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_072_landslide_education_centers
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
      from landslide (LANDSLIDE) events in Colombia. DesInventar records: 142 events
      with data out of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_073_landslide_evacuated
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
    description: 'Observed health facilities destroyed or affected from landslide
      (LANDSLIDE) events in Colombia. DesInventar records: 34 events with data out
      of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_074_landslide_hospitals
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
      landslide (LANDSLIDE) events in Colombia. DesInventar records: 2,153 events
      with data out of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_075_landslide_houses_damaged
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
      events in Colombia. DesInventar records: 2,060 events with data out of 9,041
      total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_076_landslide_houses_destroyed
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
      from landslide (LANDSLIDE) events in Colombia. DesInventar records: 749 events
      with data out of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_077_landslide_injured
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
      (LANDSLIDE) events in Colombia. DesInventar records: 205 events with data out
      of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_078_landslide_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: COP
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in US Dollars from landslide (LANDSLIDE)
      events in Colombia. DesInventar records: 4 events with data out of 9,041 total
      landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_079_landslide_losses_usd
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
    description: 'Observed livestock lost from landslide (LANDSLIDE) events in Colombia.
      DesInventar records: 4 events with data out of 9,041 total landslide events
      (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_080_landslide_lost_cattle
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
      from landslide (LANDSLIDE) events in Colombia. DesInventar records: 140 events
      with data out of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_081_landslide_missing
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
      (LANDSLIDE) events in Colombia. DesInventar records: 7 events with data out
      of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_082_landslide_relocated
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
      landslide (LANDSLIDE) events in Colombia. DesInventar records: 471 events with
      data out of 9,041 total landslide events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_083_landslide_victims
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
    asset_dimension: content
    description: 'Observed total economic losses in US Dollars from landslide (SEDIMENTATION)
      events in Colombia. DesInventar records: 1 events with data out of 12 total
      landslide events (1984-1985).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: loss_084_landslide_losses_usd
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
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from landslide (AVALANCHE) events in Colombia. DesInventar records: 23
      events with data out of 25 total landslide events (1995-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_085_landslide_affected
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
    description: 'Observed hectares of crops/woods destroyed or affected from landslide
      (AVALANCHE) events in Colombia. DesInventar records: 1 events with data out
      of 25 total landslide events (1995-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_086_landslide_damages_in_crops_ha
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
    description: 'Observed deaths directly caused by disaster events from landslide
      (AVALANCHE) events in Colombia. DesInventar records: 3 events with data out
      of 25 total landslide events (1995-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_087_landslide_deaths
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
    description: 'Observed educational facilities destroyed or affected from landslide
      (AVALANCHE) events in Colombia. DesInventar records: 2 events with data out
      of 25 total landslide events (1995-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_088_landslide_education_centers
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
      landslide (AVALANCHE) events in Colombia. DesInventar records: 14 events with
      data out of 25 total landslide events (1995-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_089_landslide_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from landslide (AVALANCHE)
      events in Colombia. DesInventar records: 12 events with data out of 25 total
      landslide events (1995-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_090_landslide_houses_destroyed
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
      from landslide (AVALANCHE) events in Colombia. DesInventar records: 3 events
      with data out of 25 total landslide events (1995-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_091_landslide_injured
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
      from landslide (AVALANCHE) events in Colombia. DesInventar records: 2 events
      with data out of 25 total landslide events (1995-2009).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_092_landslide_missing
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
      work) from strong wind (SNOWSTORM, STORM) events in Colombia. DesInventar records:
      42 events with data out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_093_strongwind_affected
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
    description: 'Observed hectares of crops/woods destroyed or affected from strong
      wind (SNOWSTORM, STORM) events in Colombia. DesInventar records: 7 events with
      data out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_094_strongwind_damages_in_crops_ha
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from strong wind
      (SNOWSTORM, STORM) events in Colombia. DesInventar records: 5 events with data
      out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_095_strongwind_damages_in_roads_mts
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
    description: 'Observed deaths directly caused by disaster events from strong wind
      (SNOWSTORM, STORM) events in Colombia. DesInventar records: 75 events with data
      out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_096_strongwind_deaths
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
    description: 'Observed educational facilities destroyed or affected from strong
      wind (SNOWSTORM, STORM) events in Colombia. DesInventar records: 17 events with
      data out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_097_strongwind_education_centers
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
      from strong wind (SNOWSTORM, STORM) events in Colombia. DesInventar records:
      4 events with data out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_098_strongwind_evacuated
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
    description: 'Observed health facilities destroyed or affected from strong wind
      (SNOWSTORM, STORM) events in Colombia. DesInventar records: 5 events with data
      out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_099_strongwind_hospitals
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
      strong wind (SNOWSTORM, STORM) events in Colombia. DesInventar records: 48 events
      with data out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_100_strongwind_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from strong wind (SNOWSTORM,
      STORM) events in Colombia. DesInventar records: 94 events with data out of 348
      total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_101_strongwind_houses_destroyed
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
      from strong wind (SNOWSTORM, STORM) events in Colombia. DesInventar records:
      54 events with data out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_102_strongwind_injured
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
    description: 'Observed total economic losses in local currency from strong wind
      (SNOWSTORM, STORM) events in Colombia. DesInventar records: 38 events with data
      out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_103_strongwind_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: COP
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in US Dollars from strong wind (SNOWSTORM,
      STORM) events in Colombia. DesInventar records: 1 events with data out of 348
      total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_104_strongwind_losses_usd
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
      from strong wind (SNOWSTORM, STORM) events in Colombia. DesInventar records:
      4 events with data out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_105_strongwind_missing
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
      strong wind (SNOWSTORM, STORM) events in Colombia. DesInventar records: 41 events
      with data out of 348 total strong wind events (1976-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_106_strongwind_victims
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
      work) from strong wind (HURRICANE) events in Colombia. DesInventar records:
      4 events with data out of 7 total strong wind events (1963-1988).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_107_strongwind_affected
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from strong wind
      (HURRICANE) events in Colombia. DesInventar records: 1 events with data out
      of 7 total strong wind events (1963-1988).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_108_strongwind_damages_in_roads_mts
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
    description: 'Observed deaths directly caused by disaster events from strong wind
      (HURRICANE) events in Colombia. DesInventar records: 3 events with data out
      of 7 total strong wind events (1963-1988).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_109_strongwind_deaths
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
      from strong wind (HURRICANE) events in Colombia. DesInventar records: 1 events
      with data out of 7 total strong wind events (1963-1988).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_110_strongwind_evacuated
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
      strong wind (HURRICANE) events in Colombia. DesInventar records: 2 events with
      data out of 7 total strong wind events (1963-1988).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_111_strongwind_houses_damaged
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
    description: 'Observed homes destroyed beyond habitability from strong wind (HURRICANE)
      events in Colombia. DesInventar records: 5 events with data out of 7 total strong
      wind events (1963-1988).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_112_strongwind_houses_destroyed
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
      from strong wind (HURRICANE) events in Colombia. DesInventar records: 1 events
      with data out of 7 total strong wind events (1963-1988).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_113_strongwind_injured
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
    description: 'Observed total economic losses in local currency from strong wind
      (HURRICANE) events in Colombia. DesInventar records: 1 events with data out
      of 7 total strong wind events (1963-1988).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_114_strongwind_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: COP
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      strong wind (HURRICANE) events in Colombia. DesInventar records: 1 events with
      data out of 7 total strong wind events (1963-1988).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_115_strongwind_victims
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
      work) from tsunami (TSUNAMI) events in Colombia. DesInventar records: 1 events
      with data out of 5 total tsunami events (1979-1979).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_116_tsunami_affected
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
      (TSUNAMI) events in Colombia. DesInventar records: 4 events with data out of
      5 total tsunami events (1979-1979).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_117_tsunami_deaths
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
    description: 'Observed health facilities destroyed or affected from tsunami (TSUNAMI)
      events in Colombia. DesInventar records: 1 events with data out of 5 total tsunami
      events (1979-1979).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_118_tsunami_hospitals
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
      tsunami (TSUNAMI) events in Colombia. DesInventar records: 5 events with data
      out of 5 total tsunami events (1979-1979).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_119_tsunami_houses_damaged
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
      events in Colombia. DesInventar records: 3 events with data out of 5 total tsunami
      events (1979-1979).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_120_tsunami_houses_destroyed
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
      from tsunami (TSUNAMI) events in Colombia. DesInventar records: 5 events with
      data out of 5 total tsunami events (1979-1979).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_121_tsunami_injured
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
      from tsunami (TSUNAMI) events in Colombia. DesInventar records: 3 events with
      data out of 5 total tsunami events (1979-1979).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: tsunami
      trigger: null
      type: tsunami
    id: loss_122_tsunami_missing
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
      work) from wildfire (FIRE) events in Colombia. DesInventar records: 893 events
      with data out of 2,588 total wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_123_wildfire_affected
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
      (FIRE) events in Colombia. DesInventar records: 10 events with data out of 2,588
      total wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_124_wildfire_damages_in_crops_ha
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from wildfire (FIRE)
      events in Colombia. DesInventar records: 1 events with data out of 2,588 total
      wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_125_wildfire_damages_in_roads_mts
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
    description: 'Observed deaths directly caused by disaster events from wildfire
      (FIRE) events in Colombia. DesInventar records: 274 events with data out of
      2,588 total wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_126_wildfire_deaths
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
      (FIRE) events in Colombia. DesInventar records: 27 events with data out of 2,588
      total wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_127_wildfire_education_centers
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
      from wildfire (FIRE) events in Colombia. DesInventar records: 18 events with
      data out of 2,588 total wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_128_wildfire_evacuated
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
    description: 'Observed health facilities destroyed or affected from wildfire (FIRE)
      events in Colombia. DesInventar records: 14 events with data out of 2,588 total
      wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_129_wildfire_hospitals
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
      wildfire (FIRE) events in Colombia. DesInventar records: 401 events with data
      out of 2,588 total wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_130_wildfire_houses_damaged
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
      events in Colombia. DesInventar records: 922 events with data out of 2,588 total
      wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_131_wildfire_houses_destroyed
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
      from wildfire (FIRE) events in Colombia. DesInventar records: 417 events with
      data out of 2,588 total wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_132_wildfire_injured
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
      events in Colombia. DesInventar records: 901 events with data out of 2,588 total
      wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_133_wildfire_losses_local
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: COP
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from wildfire (FIRE) events in Colombia.
      DesInventar records: 1 events with data out of 2,588 total wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_134_wildfire_lost_cattle
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
      from wildfire (FIRE) events in Colombia. DesInventar records: 4 events with
      data out of 2,588 total wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_135_wildfire_missing
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
      wildfire (FIRE) events in Colombia. DesInventar records: 476 events with data
      out of 2,588 total wildfire events (1984-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_136_wildfire_victims
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
purpose: To document historical disaster losses in Colombia from the DesInventar national
  disaster loss inventory, supporting disaster risk reduction monitoring under the
  Sendai Framework.
referenced_by: []
resources:
- access_url: https://data.humdata.org/dataset/baeedcfd-14c7-4028-8eb0-e1192e82dc79
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DesInventar Disaster Loss and Damage Dataset for Colombia (Disaster
    data for Colombia)
  download_url: https://data.humdata.org/dataset/baeedcfd-14c7-4028-8eb0-e1192e82dc79/resource/93b7528b-46fd-4504-9406-f4d97a59a24c/download/colombia.zip
  format: null
  id: resource_001
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Disaster data for Colombia
- access_url: https://data.humdata.org/dataset/baeedcfd-14c7-4028-8eb0-e1192e82dc79
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DesInventar Disaster Loss and Damage Dataset for Colombia (Disaster
    Tabular data for Colombia)
  download_url: https://data.humdata.org/dataset/baeedcfd-14c7-4028-8eb0-e1192e82dc79/resource/f156b3b5-97ab-48a5-b66d-5c00d56f85c9/download/di_report-colombia.xls
  format: null
  id: resource_002
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Disaster Tabular data for Colombia
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_undrr_desinventar
spatial:
  bbox:
  - -81.72
  - -4.24
  - -66.88
  - 13.58
  centroid: null
  countries:
  - COL
  gazetteer_entries:
  - description: Colombia
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/3686110/colombia.html
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: DesInventar Disaster Loss and Damage Dataset for Colombia
version: '1'
vulnerability: null
---
