---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-district-struck-by-2020-tropical-cyclone-gati
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-district-struck-by-2020-tropical-cyclone-gati
dataset_id: rdls_hzd-som_icpac_districtstruck2020tropica_202012
description: '2020 Tropical Cyclone Gati struck a couple of Somalia Districts including
  Ceerigaabo, Ceel Afweyn, Laasqoray, Bossaso, Bandarbeyla, Caluula, Qandala and Qardho
  District. On November 22-23, 2020 TC Gati made landfall in northern Somalia, becoming
  the first hurricane-equivalent storm to hit the Horn of Africa. TC Gati originated
  from the Bay of Bengal. It made landfall at Ras Hafun (Northeast of Somalia) with
  maximum sustained winds of 170Km/hr. By 25 November 2020, TC GATI had dissipated
  but it left trail of destruction across Bari and Sanaag regions. Somalia villages
  struck by the storm included Bargaal, Gumbax, Caluula, Qandala, Lasqoray, Hadaaftimo,
  Badhan, Qardho, Waaciye, Ceel Dofaar, Iskushuban, Bilke, Bandarbyla, Baar-Madobe,
  Xaafuun, Hordio, Handa, Itaageer, Ahable, Dhaankadus, Dul Xaafuun, Dardaare, Garan,
  Baarmadowe, Hurdiya, Foocaar, Afdhicin, Haluula, Kurduush, , Taageer and Xandha.
  Tropical Cyclone Gati was the strongest storm ever recorded in the northern Indian
  Ocean and wreaked unimaginable damage on people and property. GATI left a trail
  of destruction across Bari and Sanaag regions of Somalia, disproportionately affecting
  coastal communities. Authorities estimated 180,000 people (30,000 households) had
  been affected in Puntland Regional State, with 42,000 people (7,000 households)
  displaced and at least eight people killed and unknown number injured, with considerable
  damage reported to infrastructure, livelihoods, and social services (telecommunication,
  electricity, roads, schools). Resultant flooding burst sewerage system and increased
  the risk of diseases among the affected population. The worst hit areas were Baargaal,
  Foocaar, Garduush, Hurdiya, and Xaafuun, Foocaar, Garduush and Garan Hoose were
  worst hit villages in the Indian Ocean, Bosaso and Qandala in the Gulf of Aden,
  and Baarmadowe.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-district-struck-by-2020-tropical-cyclone-gati]'
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
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Administrative district boundaries for Somalia were intersected with
    the observed spatial footprint of TC Gati's impact zone following the cyclone's
    November 2020 landfall in Ras Hafun. The resulting dataset identifies which districts
    experienced direct exposure to the tropical cyclone event.
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
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-district-struck-by-2020-tropical-cyclone-gati
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2020_TCGati&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. 2020 Tropical Cyclone Gati struck a couple of
    Somalia Districts including Ceerigaabo, Ceel Afweyn, Laasqoray, Bossaso, Bandarbeyla,
    Caluula, Qandala and Qardho District. On November 22-23, 2020 TC Gati made landfall
    in northern Somalia, becoming the first hurricane-equivalent storm to hit the
    Horn of Africa. TC Gati originated from the Bay of Bengal. It made landfall at
    Ras Hafun (Northeast of Somalia) with maximum sustained winds of 170Km/hr. By
    25 November 2020, TC GATI had dissipated but it left trail of destruction across
    Bari and Sanaag regions. Somalia villages struck by the storm included Bargaal,
    Gumbax, Caluula, Qandala, Lasqoray, Hadaaftimo, Badhan, Qardho, Waaciye, Ceel
    Dofaar, Iskushuban, Bilke, Bandarbyla, Baar-Madobe, Xaafuun, Hordio, Handa, Itaageer,
    Ahable, Dhaankadus, Dul Xaafuun, Dardaare, Garan, Baarmadowe, Hurdiya, Foocaar,
    Afdhicin, Haluula, Kurduush, , Taageer and Xandha.
  download_url: null
  format: null
  id: resource_b13578d3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia District struck by 2020 Tropical Cyclone Gati Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2020_TCGati&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. 2020 Tropical Cyclone Gati struck a couple of Somalia Districts
    including Ceerigaabo, Ceel Afweyn, Laasqoray, Bossaso, Bandarbeyla, Caluula, Qandala
    and Qardho District. On November 22-23, 2020 TC Gati made landfall in northern
    Somalia, becoming the first hurricane-equivalent storm to hit the Horn of Africa.
    TC Gati originated from the Bay of Bengal. It made landfall at Ras Hafun (Northeast
    of Somalia) with maximum sustained winds of 170Km/hr. By 25 November 2020, TC
    GATI had dissipated but it left trail of destruction across Bari and Sanaag regions.
    Somalia villages struck by the storm included Bargaal, Gumbax, Caluula, Qandala,
    Lasqoray, Hadaaftimo, Badhan, Qardho, Waaciye, Ceel Dofaar, Iskushuban, Bilke,
    Bandarbyla, Baar-Madobe, Xaafuun, Hordio, Handa, Itaageer, Ahable, Dhaankadus,
    Dul Xaafuun, Dardaare, Garan, Baarmadowe, Hurdiya, Foocaar, Afdhicin, Haluula,
    Kurduush, , Taageer and Xandha.
  download_url: null
  format: null
  id: resource_200bc108
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia District struck by 2020 Tropical Cyclone Gati CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2020_TCGati&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. 2020 Tropical Cyclone Gati struck a couple of Somalia Districts
    including Ceerigaabo, Ceel Afweyn, Laasqoray, Bossaso, Bandarbeyla, Caluula, Qandala
    and Qardho District. On November 22-23, 2020 TC Gati made landfall in northern
    Somalia, becoming the first hurricane-equivalent storm to hit the Horn of Africa.
    TC Gati originated from the Bay of Bengal. It made landfall at Ras Hafun (Northeast
    of Somalia) with maximum sustained winds of 170Km/hr. By 25 November 2020, TC
    GATI had dissipated but it left trail of destruction across Bari and Sanaag regions.
    Somalia villages struck by the storm included Bargaal, Gumbax, Caluula, Qandala,
    Lasqoray, Hadaaftimo, Badhan, Qardho, Waaciye, Ceel Dofaar, Iskushuban, Bilke,
    Bandarbyla, Baar-Madobe, Xaafuun, Hordio, Handa, Itaageer, Ahable, Dhaankadus,
    Dul Xaafuun, Dardaare, Garan, Baarmadowe, Hurdiya, Foocaar, Afdhicin, Haluula,
    Kurduush, , Taageer and Xandha.
  download_url: null
  format: null
  id: resource_d6eed29a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia District struck by 2020 Tropical Cyclone Gati Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2020_TCGati&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. 2020 Tropical Cyclone Gati struck a couple of Somalia
    Districts including Ceerigaabo, Ceel Afweyn, Laasqoray, Bossaso, Bandarbeyla,
    Caluula, Qandala and Qardho District. On November 22-23, 2020 TC Gati made landfall
    in northern Somalia, becoming the first hurricane-equivalent storm to hit the
    Horn of Africa. TC Gati originated from the Bay of Bengal. It made landfall at
    Ras Hafun (Northeast of Somalia) with maximum sustained winds of 170Km/hr. By
    25 November 2020, TC GATI had dissipated but it left trail of destruction across
    Bari and Sanaag regions. Somalia villages struck by the storm included Bargaal,
    Gumbax, Caluula, Qandala, Lasqoray, Hadaaftimo, Badhan, Qardho, Waaciye, Ceel
    Dofaar, Iskushuban, Bilke, Bandarbyla, Baar-Madobe, Xaafuun, Hordio, Handa, Itaageer,
    Ahable, Dhaankadus, Dul Xaafuun, Dardaare, Garan, Baarmadowe, Hurdiya, Foocaar,
    Afdhicin, Haluula, Kurduush, , Taageer and Xandha.
  download_url: null
  format: null
  id: resource_b867d605
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia District struck by 2020 Tropical Cyclone Gati GeoJSON
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_icpac_districtstruck2020tropica_202012
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
  end: '2020-12-25'
  start: '2020-12-22'
temporal_resolution: null
title: Somalia District struck by 2020 Tropical Cyclone Gati
version: null
vulnerability: null
---
