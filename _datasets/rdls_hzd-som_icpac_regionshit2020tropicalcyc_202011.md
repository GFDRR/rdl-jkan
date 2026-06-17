---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2020-tropical-cyclone-gati
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2020-tropical-cyclone-gati
dataset_id: rdls_hzd-som_icpac_regionshit2020tropicalcyc_202011
description: 'Tropical Cyclone Gati originated from the Bay of Bengal. On 22 November
  2020 at around 13:00 UTC, TC Gati became the strongest ever documented tropical
  storm to hit Somalia. Gati made landfall at Ras Hafun (Northeast of Somalia) with
  maximum sustained winds of 170Km/hr and was classified as a Category 2 storm (or
  category 2 hurricane on the Saffir-Simpson scale). This layers shows the occurence
  of TC Gati in two regions of Somali, Sanaag and Bari Regions. TC Gati primarily
  impacted parts of Bari region in Puntland State and then Sanaag region in Somaliland.
  Authorities reported rainfall totals from the storm to be greater than the amounts
  normally seen for the whole year. In a 24-hour period, Bosaso recorded 128mm of
  rain and Balidhidin 103mm. By 25th November 2020, TC Gati had dissipated but it
  left trail of destruction across Bari and Sanaag regions of Somalia. Authorities
  estimated 180,000 people (30,000 households) had been affected in Puntland Regional
  State, with 42,000 people (7,000 households) displaced and at least eight people
  killed and unknown number injured, with considerable damages reported to infrastructure,
  livelihoods, and social services (telecommunication, electricity, roads, schools).
  Resultant flooding bursted the sewerage system and increased risk of diseases among
  the affected population. By the end of December, the storm had killed 9 people and
  over 63 000 livestock (sheep and goats), and affected around 183 000 people. The
  heavy rains caused the Ceel-Daahir River in Puntland to flood, blocking vehicles
  from bringing crucial supplies. In some towns such as Xaafun, Hurdiye, and Karduush
  people reported losing their entire herds of livestock. There were also reports
  of the destruction of 120 fishing vessels in these areas resulting in the loss of
  livelihood for an estimated 460 fishermen.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2020-tropical-cyclone-gati]'
details: null
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
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Observed tropical cyclone event data from ICPAC documenting the November
    2020 TC Gati landfall in Somalia. The dataset captures the spatial extent of cyclone
    impact across Bari and Sanaag regions with recorded maximum sustained winds of
    170 km/hr at landfall near Ras Hafun, providing post-event hazard characterization
    for this extreme wind event.
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Center (ICPAC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2020-tropical-cyclone-gati
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2020_TC_Gati&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. Tropical Cyclone Gati originated from the Bay
    of Bengal. On 22 November 2020 at around 13:00 UTC, TC Gati became the strongest
    ever documented tropical storm to hit Somalia. Gati made landfall at Ras Hafun
    (Northeast of Somalia) with maximum sustained winds of 170Km/hr and was classified
    as a Category 2 storm (or category 2 hurricane on the Saffir-Simpson scale). This
    layers shows the occurence of TC Gati in two regions of Somali, Sanaag and Bari
    Regions.
  download_url: null
  format: null
  id: resource_3c12aa93
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2020 Tropical Cyclone Gati Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2020_TC_Gati&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. Tropical Cyclone Gati originated from the Bay of Bengal.
    On 22 November 2020 at around 13:00 UTC, TC Gati became the strongest ever documented
    tropical storm to hit Somalia. Gati made landfall at Ras Hafun (Northeast of Somalia)
    with maximum sustained winds of 170Km/hr and was classified as a Category 2 storm
    (or category 2 hurricane on the Saffir-Simpson scale). This layers shows the occurence
    of TC Gati in two regions of Somali, Sanaag and Bari Regions.
  download_url: null
  format: null
  id: resource_3a23a9e2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2020 Tropical Cyclone Gati CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2020_TC_Gati&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. Tropical Cyclone Gati originated from the Bay of Bengal.
    On 22 November 2020 at around 13:00 UTC, TC Gati became the strongest ever documented
    tropical storm to hit Somalia. Gati made landfall at Ras Hafun (Northeast of Somalia)
    with maximum sustained winds of 170Km/hr and was classified as a Category 2 storm
    (or category 2 hurricane on the Saffir-Simpson scale). This layers shows the occurence
    of TC Gati in two regions of Somali, Sanaag and Bari Regions.
  download_url: null
  format: null
  id: resource_fbe9671f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2020 Tropical Cyclone Gati Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2020_TC_Gati&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. Tropical Cyclone Gati originated from the Bay of Bengal.
    On 22 November 2020 at around 13:00 UTC, TC Gati became the strongest ever documented
    tropical storm to hit Somalia. Gati made landfall at Ras Hafun (Northeast of Somalia)
    with maximum sustained winds of 170Km/hr and was classified as a Category 2 storm
    (or category 2 hurricane on the Saffir-Simpson scale). This layers shows the occurence
    of TC Gati in two regions of Somali, Sanaag and Bari Regions.
  download_url: null
  format: null
  id: resource_9f17cac8
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2020 Tropical Cyclone Gati GeoJSON
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_icpac_regionshit2020tropicalcyc_202011
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
  end: '2020-11-25'
  start: '2020-11-22'
temporal_resolution: null
title: Somalia Regions hit by 2020 Tropical Cyclone Gati
version: null
vulnerability: null
---
