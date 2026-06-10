---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: General Directorate of Civil Emergencies
  url: 'More information can be found here: http://www.mbrojtjacivile.al/'
creator:
  affiliation: null
  email: isdr@un.org
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://www.desinventar.net/
dataset_id: rdls_lss-alb_undrr_desinventar
description: 'National disaster loss inventory for Albania from the DesInventar Sendai
  Framework Monitor database, compiled by General Directorate of Civil Emergencies
  and published by the United Nations Office for Disaster Risk Reduction (UNDRR).
  Contains 4,659 event-level loss records covering 1973-2015, with observed impacts
  from coastal_flood, convective_storm, drought, earthquake, extreme_temperature,
  flood, landslide, strong_wind, wildfire events. Loss data includes human casualties,
  displacement, building damage, economic losses, agricultural damage, and infrastructure
  impacts. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX) at https://data.humdata.org] [Original dataset: https://data.humdata.org/dataset/01c902dd-fec3-499b-a6c0-d092c18bc73e]'
details: 'Event-level disaster loss records from the DesInventar database for Albania,
  maintained by General Directorate of Civil Emergencies. Covers 4,659 observed disaster
  events from 1973-2015. Data collected through direct observational reporting and
  includes human impacts (deaths, injuries, missing, affected, evacuated, relocated),
  physical impacts (houses destroyed/damaged, education centres, hospitals, roads),
  economic losses (local currency and USD), and agricultural impacts (crop damage
  in hectares, livestock losses). Methodology: Direct Observational Data / Anecdotal
  Data.'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
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
    url: https://data.humdata.org/dataset/01c902dd-fec3-499b-a6c0-d092c18bc73e
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/01c902dd-fec3-499b-a6c0-d092c18bc73e
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      coastal flood (SURGE) events in Albania. DesInventar records: 2 events with
      data out of 7 total coastal flood events (1975-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: storm_surge
      trigger: null
      type: flood
    id: loss_001_coastalflood_houses_damaged
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from convective
      storm (HAILSTORM, THUNDERSTORM) events in Albania. DesInventar records: 79 events
      with data out of 217 total convective storm events (1976-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_002_convectivestorm_damages_in_crops_ha
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from convective
      storm (HAILSTORM, THUNDERSTORM) events in Albania. DesInventar records: 54 events
      with data out of 217 total convective storm events (1976-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_003_convectivestorm_deaths
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      convective storm (HAILSTORM, THUNDERSTORM) events in Albania. DesInventar records:
      2 events with data out of 217 total convective storm events (1976-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_004_convectivestorm_houses_damaged
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from convective storm
      (HAILSTORM, THUNDERSTORM) events in Albania. DesInventar records: 2 events with
      data out of 217 total convective storm events (1976-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_005_convectivestorm_houses_destroyed
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from convective storm (HAILSTORM, THUNDERSTORM) events in Albania. DesInventar
      records: 19 events with data out of 217 total convective storm events (1976-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_006_convectivestorm_injured
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from convective
      storm (HAILSTORM, THUNDERSTORM) events in Albania. DesInventar records: 20 events
      with data out of 217 total convective storm events (1976-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_007_convectivestorm_losses_local
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from convective storm (HAILSTORM, THUNDERSTORM)
      events in Albania. DesInventar records: 18 events with data out of 217 total
      convective storm events (1976-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_008_convectivestorm_lost_cattle
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      convective storm (HAILSTORM, THUNDERSTORM) events in Albania. DesInventar records:
      1 events with data out of 217 total convective storm events (1976-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: tornado
      trigger: null
      type: convective_storm
    id: loss_009_convectivestorm_victims
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from drought
      (DROUGHT) events in Albania. DesInventar records: 1 events with data out of
      1 total drought events (1993-1993).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: loss_010_drought_damages_in_crops_ha
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from earthquake (EARTHQUAKE) events in Albania. DesInventar records: 8
      events with data out of 185 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_011_earthquake_affected
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from earthquake
      (EARTHQUAKE) events in Albania. DesInventar records: 1 events with data out
      of 185 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_012_earthquake_damages_in_roads_mts
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from earthquake
      (EARTHQUAKE) events in Albania. DesInventar records: 14 events with data out
      of 185 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_013_earthquake_deaths
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed educational facilities destroyed or affected from earthquake
      (EARTHQUAKE) events in Albania. DesInventar records: 8 events with data out
      of 185 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_014_earthquake_education_centers
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons temporarily evacuated from homes or workplaces
      from earthquake (EARTHQUAKE) events in Albania. DesInventar records: 5 events
      with data out of 185 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_015_earthquake_evacuated
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed health facilities destroyed or affected from earthquake
      (EARTHQUAKE) events in Albania. DesInventar records: 5 events with data out
      of 185 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_016_earthquake_hospitals
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      earthquake (EARTHQUAKE) events in Albania. DesInventar records: 92 events with
      data out of 185 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_017_earthquake_houses_damaged
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from earthquake (EARTHQUAKE)
      events in Albania. DesInventar records: 66 events with data out of 185 total
      earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_018_earthquake_houses_destroyed
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from earthquake (EARTHQUAKE) events in Albania. DesInventar records: 18 events
      with data out of 185 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_019_earthquake_injured
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from earthquake
      (EARTHQUAKE) events in Albania. DesInventar records: 78 events with data out
      of 185 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_020_earthquake_losses_local
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      earthquake (EARTHQUAKE) events in Albania. DesInventar records: 26 events with
      data out of 185 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: loss_021_earthquake_victims
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      earthquake (LIQUEFACTION) events in Albania. DesInventar records: 2 events with
      data out of 4 total earthquake events (2014-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: MMI:-
      process: liquefaction
      trigger: null
      type: earthquake
    id: loss_022_earthquake_victims
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from extreme
      temperature (COLD WAVE, FROST) events in Albania. DesInventar records: 55 events
      with data out of 126 total extreme temperature events (1990-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_023_extremetemperature_damages_in_crops_ha
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from extreme
      temperature (COLD WAVE, FROST) events in Albania. DesInventar records: 10 events
      with data out of 126 total extreme temperature events (1990-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_024_extremetemperature_deaths
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      extreme temperature (COLD WAVE, FROST) events in Albania. DesInventar records:
      2 events with data out of 126 total extreme temperature events (1990-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_025_extremetemperature_houses_damaged
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from extreme temperature (COLD WAVE, FROST) events in Albania. DesInventar records:
      10 events with data out of 126 total extreme temperature events (1990-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_026_extremetemperature_injured
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from extreme temperature
      (COLD WAVE, FROST) events in Albania. DesInventar records: 5 events with data
      out of 126 total extreme temperature events (1990-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_027_extremetemperature_losses_local
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from extreme temperature (COLD WAVE, FROST)
      events in Albania. DesInventar records: 10 events with data out of 126 total
      extreme temperature events (1990-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: loss_028_extremetemperature_lost_cattle
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from extreme
      temperature (HEAT WAVE) events in Albania. DesInventar records: 9 events with
      data out of 22 total extreme temperature events (1998-2002).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: AirTemp:C
      process: extreme_heat
      trigger: null
      type: extreme_temperature
    id: loss_029_extremetemperature_deaths
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from extreme temperature (HEAT WAVE) events in Albania. DesInventar records:
      11 events with data out of 22 total extreme temperature events (1998-2002).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: AirTemp:C
      process: extreme_heat
      trigger: null
      type: extreme_temperature
    id: loss_030_extremetemperature_injured
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from extreme temperature (HEAT WAVE) events
      in Albania. DesInventar records: 1 events with data out of 22 total extreme
      temperature events (1998-2002).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: AirTemp:C
      process: extreme_heat
      trigger: null
      type: extreme_temperature
    id: loss_031_extremetemperature_lost_cattle
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from flood (FLASH FLOOD, FLOOD) events in Albania. DesInventar records:
      18 events with data out of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_032_flood_affected
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from flood
      (FLASH FLOOD, FLOOD) events in Albania. DesInventar records: 474 events with
      data out of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_033_flood_damages_in_crops_ha
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from flood (FLASH
      FLOOD, FLOOD) events in Albania. DesInventar records: 19 events with data out
      of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_034_flood_damages_in_roads_mts
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from flood (FLASH
      FLOOD, FLOOD) events in Albania. DesInventar records: 44 events with data out
      of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_035_flood_deaths
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed educational facilities destroyed or affected from flood
      (FLASH FLOOD, FLOOD) events in Albania. DesInventar records: 13 events with
      data out of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_036_flood_education_centers
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons temporarily evacuated from homes or workplaces
      from flood (FLASH FLOOD, FLOOD) events in Albania. DesInventar records: 76 events
      with data out of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_037_flood_evacuated
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed health facilities destroyed or affected from flood (FLASH
      FLOOD, FLOOD) events in Albania. DesInventar records: 2 events with data out
      of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_038_flood_hospitals
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      flood (FLASH FLOOD, FLOOD) events in Albania. DesInventar records: 208 events
      with data out of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_039_flood_houses_damaged
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from flood (FLASH FLOOD,
      FLOOD) events in Albania. DesInventar records: 96 events with data out of 949
      total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_040_flood_houses_destroyed
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from flood (FLASH FLOOD, FLOOD) events in Albania. DesInventar records: 18 events
      with data out of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_041_flood_injured
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from flood (FLASH
      FLOOD, FLOOD) events in Albania. DesInventar records: 225 events with data out
      of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_042_flood_losses_local
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in US Dollars from flood (FLASH FLOOD,
      FLOOD) events in Albania. DesInventar records: 4 events with data out of 949
      total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_043_flood_losses_usd
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from flood (FLASH FLOOD, FLOOD) events in
      Albania. DesInventar records: 96 events with data out of 949 total flood events
      (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_044_flood_lost_cattle
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons missing or unaccounted for after disaster events
      from flood (FLASH FLOOD, FLOOD) events in Albania. DesInventar records: 1 events
      with data out of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_045_flood_missing
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons permanently relocated from homes from flood (FLASH
      FLOOD, FLOOD) events in Albania. DesInventar records: 4 events with data out
      of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_046_flood_relocated
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      flood (FLASH FLOOD, FLOOD) events in Albania. DesInventar records: 129 events
      with data out of 949 total flood events (2002-2015).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: loss_047_flood_victims
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from flood (RAINS) events in Albania. DesInventar records: 1 events with
      data out of 217 total flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_048_flood_affected
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from flood
      (RAINS) events in Albania. DesInventar records: 49 events with data out of 217
      total flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_049_flood_damages_in_crops_ha
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from flood (RAINS)
      events in Albania. DesInventar records: 4 events with data out of 217 total
      flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_050_flood_damages_in_roads_mts
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from flood (RAINS)
      events in Albania. DesInventar records: 3 events with data out of 217 total
      flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_051_flood_deaths
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed educational facilities destroyed or affected from flood
      (RAINS) events in Albania. DesInventar records: 2 events with data out of 217
      total flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_052_flood_education_centers
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons temporarily evacuated from homes or workplaces
      from flood (RAINS) events in Albania. DesInventar records: 2 events with data
      out of 217 total flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_053_flood_evacuated
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      flood (RAINS) events in Albania. DesInventar records: 40 events with data out
      of 217 total flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_054_flood_houses_damaged
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from flood (RAINS)
      events in Albania. DesInventar records: 43 events with data out of 217 total
      flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_055_flood_houses_destroyed
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from flood (RAINS) events in Albania. DesInventar records: 2 events with data
      out of 217 total flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_056_flood_injured
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from flood (RAINS)
      events in Albania. DesInventar records: 57 events with data out of 217 total
      flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_057_flood_losses_local
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from flood (RAINS) events in Albania. DesInventar
      records: 3 events with data out of 217 total flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_058_flood_lost_cattle
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons missing or unaccounted for after disaster events
      from flood (RAINS) events in Albania. DesInventar records: 1 events with data
      out of 217 total flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_059_flood_missing
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      flood (RAINS) events in Albania. DesInventar records: 42 events with data out
      of 217 total flood events (2007-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: wd:m
      process: pluvial_flood
      trigger: null
      type: flood
    id: loss_060_flood_victims
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from landslide (LANDSLIDE) events in Albania. DesInventar records: 5 events
      with data out of 629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_061_landslide_affected
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from landslide
      (LANDSLIDE) events in Albania. DesInventar records: 17 events with data out
      of 629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_062_landslide_damages_in_crops_ha
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from landslide (LANDSLIDE)
      events in Albania. DesInventar records: 30 events with data out of 629 total
      landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_063_landslide_damages_in_roads_mts
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from landslide
      (LANDSLIDE) events in Albania. DesInventar records: 40 events with data out
      of 629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_064_landslide_deaths
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed educational facilities destroyed or affected from landslide
      (LANDSLIDE) events in Albania. DesInventar records: 7 events with data out of
      629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_065_landslide_education_centers
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons temporarily evacuated from homes or workplaces
      from landslide (LANDSLIDE) events in Albania. DesInventar records: 29 events
      with data out of 629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_066_landslide_evacuated
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      landslide (LANDSLIDE) events in Albania. DesInventar records: 117 events with
      data out of 629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_067_landslide_houses_damaged
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from landslide (LANDSLIDE)
      events in Albania. DesInventar records: 346 events with data out of 629 total
      landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_068_landslide_houses_destroyed
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from landslide (LANDSLIDE) events in Albania. DesInventar records: 15 events
      with data out of 629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_069_landslide_injured
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from landslide
      (LANDSLIDE) events in Albania. DesInventar records: 306 events with data out
      of 629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_070_landslide_losses_local
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in US Dollars from landslide (LANDSLIDE)
      events in Albania. DesInventar records: 1 events with data out of 629 total
      landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_071_landslide_losses_usd
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from landslide (LANDSLIDE) events in Albania.
      DesInventar records: 3 events with data out of 629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_072_landslide_lost_cattle
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons permanently relocated from homes from landslide
      (LANDSLIDE) events in Albania. DesInventar records: 5 events with data out of
      629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_073_landslide_relocated
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      landslide (LANDSLIDE) events in Albania. DesInventar records: 249 events with
      data out of 629 total landslide events (1995-2013).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: loss_074_landslide_victims
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from landslide
      (SEDIMENTATION) events in Albania. DesInventar records: 2 events with data out
      of 3 total landslide events (1999-2005).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: loss_075_landslide_damages_in_crops_ha
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from landslide
      (AVALANCHE) events in Albania. DesInventar records: 17 events with data out
      of 25 total landslide events (2010-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_076_landslide_deaths
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      landslide (AVALANCHE) events in Albania. DesInventar records: 3 events with
      data out of 25 total landslide events (2010-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_077_landslide_houses_damaged
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from landslide (AVALANCHE)
      events in Albania. DesInventar records: 3 events with data out of 25 total landslide
      events (2010-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_078_landslide_houses_destroyed
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from landslide (AVALANCHE) events in Albania. DesInventar records: 8 events
      with data out of 25 total landslide events (2010-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_079_landslide_injured
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from landslide
      (AVALANCHE) events in Albania. DesInventar records: 2 events with data out of
      25 total landslide events (2010-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_080_landslide_losses_local
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from landslide (AVALANCHE) events in Albania.
      DesInventar records: 3 events with data out of 25 total landslide events (2010-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_081_landslide_lost_cattle
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons missing or unaccounted for after disaster events
      from landslide (AVALANCHE) events in Albania. DesInventar records: 2 events
      with data out of 25 total landslide events (2010-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_082_landslide_missing
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      landslide (AVALANCHE) events in Albania. DesInventar records: 1 events with
      data out of 25 total landslide events (2010-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: LSI:-
      process: snow_avalanche
      trigger: null
      type: landslide
    id: loss_083_landslide_victims
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from strong wind (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar
      records: 55 events with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_084_strongwind_affected
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from strong
      wind (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar records: 50
      events with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_085_strongwind_damages_in_crops_ha
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed metres of transport networks destroyed from strong wind
      (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar records: 4 events
      with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_086_strongwind_damages_in_roads_mts
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from strong wind
      (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar records: 45 events
      with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_087_strongwind_deaths
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed educational facilities destroyed or affected from strong
      wind (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar records: 28
      events with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_088_strongwind_education_centers
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons temporarily evacuated from homes or workplaces
      from strong wind (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar
      records: 16 events with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_089_strongwind_evacuated
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed health facilities destroyed or affected from strong wind
      (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar records: 1 events
      with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_090_strongwind_hospitals
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      strong wind (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar records:
      86 events with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_091_strongwind_houses_damaged
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from strong wind (SNOWSTORM,
      STORM, WINDSTORM) events in Albania. DesInventar records: 108 events with data
      out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_092_strongwind_houses_destroyed
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from strong wind (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar
      records: 26 events with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_093_strongwind_injured
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from strong wind
      (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar records: 130 events
      with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_094_strongwind_losses_local
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from strong wind (SNOWSTORM, STORM, WINDSTORM)
      events in Albania. DesInventar records: 65 events with data out of 891 total
      strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_095_strongwind_lost_cattle
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons missing or unaccounted for after disaster events
      from strong wind (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar
      records: 4 events with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_096_strongwind_missing
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      strong wind (SNOWSTORM, STORM, WINDSTORM) events in Albania. DesInventar records:
      88 events with data out of 891 total strong wind events (1973-2012).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_097_strongwind_victims
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons indirectly affected (disruption to services, commerce,
      work) from wildfire (FIRE, FOREST FIRE) events in Albania. DesInventar records:
      4 events with data out of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_098_wildfire_affected
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed hectares of crops/woods destroyed or affected from wildfire
      (FIRE, FOREST FIRE) events in Albania. DesInventar records: 716 events with
      data out of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_099_wildfire_damages_in_crops_ha
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed deaths directly caused by disaster events from wildfire
      (FIRE, FOREST FIRE) events in Albania. DesInventar records: 13 events with data
      out of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_100_wildfire_deaths
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed educational facilities destroyed or affected from wildfire
      (FIRE, FOREST FIRE) events in Albania. DesInventar records: 1 events with data
      out of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_101_wildfire_education_centers
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons temporarily evacuated from homes or workplaces
      from wildfire (FIRE, FOREST FIRE) events in Albania. DesInventar records: 5
      events with data out of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_102_wildfire_evacuated
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Observed health facilities destroyed or affected from wildfire (FIRE,
      FOREST FIRE) events in Albania. DesInventar records: 1 events with data out
      of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_103_wildfire_hospitals
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes with non-structural damage, still habitable from
      wildfire (FIRE, FOREST FIRE) events in Albania. DesInventar records: 60 events
      with data out of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_104_wildfire_houses_damaged
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: 'Observed homes destroyed beyond habitability from wildfire (FIRE,
      FOREST FIRE) events in Albania. DesInventar records: 46 events with data out
      of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_105_wildfire_houses_destroyed
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons injured or made sick directly by disaster events
      from wildfire (FIRE, FOREST FIRE) events in Albania. DesInventar records: 6
      events with data out of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_106_wildfire_injured
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in local currency from wildfire (FIRE,
      FOREST FIRE) events in Albania. DesInventar records: 65 events with data out
      of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_107_wildfire_losses_local
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: content
    description: 'Observed total economic losses in US Dollars from wildfire (FIRE,
      FOREST FIRE) events in Albania. DesInventar records: 23 events with data out
      of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_108_wildfire_losses_usd
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: 'Observed livestock lost from wildfire (FIRE, FOREST FIRE) events
      in Albania. DesInventar records: 11 events with data out of 1,383 total wildfire
      events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_109_wildfire_lost_cattle
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons permanently relocated from homes from wildfire
      (FIRE, FOREST FIRE) events in Albania. DesInventar records: 5 events with data
      out of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_110_wildfire_relocated
    impact_and_losses:
      impact: null
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: 'Observed persons whose goods/services suffered serious damage from
      wildfire (FIRE, FOREST FIRE) events in Albania. DesInventar records: 37 events
      with data out of 1,383 total wildfire events (2003-2014).'
    disaster_identifiers: []
    hazard:
      classification: null
      id: TODO
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: loss_111_wildfire_victims
    impact_and_losses:
      impact: null
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
purpose: To document historical disaster losses in Albania from the DesInventar national
  disaster loss inventory, supporting disaster risk reduction monitoring under the
  Sendai Framework.
referenced_by: []
resources:
- access_url: https://data.humdata.org/dataset/01c902dd-fec3-499b-a6c0-d092c18bc73e
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster data for Albania
  download_url: https://data.humdata.org/dataset/01c902dd-fec3-499b-a6c0-d092c18bc73e/resource/6850c4bf-cceb-4975-8716-8a5108ad82c3/download/albania.zip
  format: null
  id: resource_001
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Disaster data for Albania
- access_url: https://data.humdata.org/dataset/01c902dd-fec3-499b-a6c0-d092c18bc73e
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster Tabular data for Albania
  download_url: https://data.humdata.org/dataset/01c902dd-fec3-499b-a6c0-d092c18bc73e/resource/0d9d729f-658c-4e7d-bbf7-f2558e8a9715/download/di_report-albania.xls
  format: null
  id: resource_002
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Disaster Tabular data for Albania
risk_data_type:
- loss
schema: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
slug: rdls_lss-alb_undrr_desinventar
spatial:
  bbox:
  - 19.27
  - 39.64
  - 21.04
  - 42.65
  centroid: null
  countries:
  - ALB
  gazetteer_entries:
  - description: Albania
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/783754/albania.html
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: DesInventar Disaster Loss and Damage Dataset for Albania
version: '1'
vulnerability: null
---
