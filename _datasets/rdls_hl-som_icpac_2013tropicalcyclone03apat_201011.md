---
attributions:
- entity:
    affiliation: null
    email: null
    name: IGAD Climate Prediction and Applications Centre (ICPAC)
    url: https://data.humdata.org/dataset/icpac-geonode-2013-tropical-cyclone-03a-path
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-2013-tropical-cyclone-03a-path
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-2013-tropical-cyclone-03a-path
dataset_id: rdls_hl-som_icpac_2013tropicalcyclone03apat_201011
description: 'This layer shows the movement path of Tropical Cyclone 03A. 2013 TC03A
  formed off the north-east coast of Somalia across the Indian Ocean, moving directly
  towards the coast of the country in the following days. The storm produced a wind
  speed of 74 kph (46 mph) and (100-200)mm of rain. It caused heavy rains with flooding
  and gale force winds in the Somali region of Puntland. The cyclone caused loss of
  human lives and the destruction of assets including livestock and fishing boats,
  destroyed numerous settlements, service centers, roads, schools, communication and
  electrical installations. The most affected areas included, Dangorayo, Bandar Beyla,
  Garowe and Eyl districts. Other areas affected include the coastal villages in Bari
  region including Hafun, Iskushuban, Bargal, Qandala and Allula districts. It was
  estimated that overall, 142,380 persons were affected by the disasters, with 8,523
  households being worst hit and 1,435 households having lost all their livestock.
  It was also reported that there were approximately 80 deaths mostly of children
  and the elderly who were most vulnerable to hypothermia and exposure. Makeshift
  structures for pastoralists were conspicuously absent or just frames, likely destroyed
  or damaged by high winds and rains. Numerous water sources were flooded, no longer
  serviceable or contaminated in some areas. There were unconfirmed disease outbreaks
  and contamination of water sources from decaying animal remains. Thousands of livestock
  were reported dead as a consequence of icy rain, which was noted in the aerial assessment.
  FAO estimated 800,000 livestock were in the affected area. Anecdotal evidence suggested
  a less than 10 per cent survival rate for livestock in the hardest hit areas.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-2013-tropical-cyclone-03a-path]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: vmax:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Observed tropical cyclone track data collected and compiled by ICPAC
    from meteorological monitoring of TC 03A in 2013, including temporal-spatial coordinates,
    maximum sustained wind speeds, minimum sea level pressure, and associated rainfall
    measurements across the Indian Ocean and Somali coast.
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Centre (ICPAC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-2013-tropical-cyclone-03a-path
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage from tropical cyclone winds including
      roads, communication and electrical installations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: vmax:m/s
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from cyclone-induced flooding and heavy rainfall
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: vmax:m/s
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  - asset_category: agriculture
    asset_dimension: product
    description: Direct loss of livestock and fishing boats from tropical cyclone
      impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: vmax:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Loss of human lives from tropical cyclone impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: vmax:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
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
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC_3A0&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. This layer shows the movement path of Tropical Cyclone 03A.
    2013 TC03A formed off the north-east coast of Somalia across the Indian Ocean,
    moving directly towards the coast of the country in the following days. The storm
    produced a wind speed of 74 kph (46 mph) and (100-200)mm of rain. It caused heavy
    rains with flooding and gale force winds in the Somali region of Puntland.
  download_url: null
  format: null
  id: resource_619344e0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2013 Tropical Cyclone 03A Path CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC_3A0&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. This layer shows the movement path of Tropical Cyclone
    03A. 2013 TC03A formed off the north-east coast of Somalia across the Indian Ocean,
    moving directly towards the coast of the country in the following days. The storm
    produced a wind speed of 74 kph (46 mph) and (100-200)mm of rain. It caused heavy
    rains with flooding and gale force winds in the Somali region of Puntland.
  download_url: null
  format: null
  id: resource_035b4616
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2013 Tropical Cyclone 03A Path Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC_3A0&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. This layer shows the movement path of Tropical Cyclone
    03A. 2013 TC03A formed off the north-east coast of Somalia across the Indian Ocean,
    moving directly towards the coast of the country in the following days. The storm
    produced a wind speed of 74 kph (46 mph) and (100-200)mm of rain. It caused heavy
    rains with flooding and gale force winds in the Somali region of Puntland.
  download_url: null
  format: null
  id: resource_18b2592e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2013 Tropical Cyclone 03A Path GeoJSON
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2013_TC_3A0&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. This layer shows the movement path of Tropical
    Cyclone 03A. 2013 TC03A formed off the north-east coast of Somalia across the
    Indian Ocean, moving directly towards the coast of the country in the following
    days. The storm produced a wind speed of 74 kph (46 mph) and (100-200)mm of rain.
    It caused heavy rains with flooding and gale force winds in the Somali region
    of Puntland.
  download_url: null
  format: null
  id: resource_4975b99a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2013 Tropical Cyclone 03A Path Zipped Shapefile
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_icpac_2013tropicalcyclone03apat_201011
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2010-11-13'
  start: '2010-11-08'
temporal_resolution: null
title: Somalia - 2013 Tropical Cyclone 03A Path
version: null
vulnerability: null
---
