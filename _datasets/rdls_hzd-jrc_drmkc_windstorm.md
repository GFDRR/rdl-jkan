---
catalog: null
contact_point:
  email: thomas.roeoesli@usys.ethz.ch
  name: "Thomas R\xF6\xF6sli"
  url: http://www.wcr.ethz.ch/
creator:
  name: Weather and Climate Risks Group, ETH Zurich
  url: http://www.wcr.ethz.ch/
dataset_id: rdls_hzd-jrc_drmkc_windstorm
description: Windstorm hazard event set containing maximum wind gust speed per event
  on a 4.4 km geographical grid.
details: 'This data archive is publishing a probabilistic extension of the historic
  windstorm hazard event set by Windstorm Information Service. The methodology used
  to create this data archive is documented in the publication: "Comparing an insurer''s
  perspective on building damages with modelled damages from pan-European winter windstorm
  event sets: a case study from Zurich, Switzerland" by Welker, Ch, Roosli, T and
  Bresch D N (2021).Windstorm hazard event set containing maximum wind gust speed
  per event on a 4.4 km geographical grid. The hazard event set covers Europe, but
  is divided into one file per country (ISO 3166-1 definition). Each file contains
  Latitude and Longitude coordinates describing the geographical grid. Event-ID and
  further metadata describing each event and a matrix reporting the maximum wind gust
  speed in Meters per Second [m/s] per event and grid coordinate.'
exposure: null
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: strong_wind
  intensity: PGWS_tcy:km/h
  occurrence_range: ''
  processes: extratropical_cyclone
license: CC-BY-4.0
loss: null
project: null
publisher:
  name: Federal Institute of Technology in Zurich (ETH Zurich)
  url: http://www.wcr.ethz.ch/
purpose: Assessment of probabilistic windstorm hazard across Europe with maximum wind
  gust speed data for risk and damage evaluation.
resources:
- coordinate_system: EPSG:4326
  description: "HDF5 container with European windstorm hazard events on a ~4.4 km\
    \ grid for country XXX (ISO3). Includes datasets: (1) event_id \u2013 unique event\
    \ identifier; (2) frequency \u2013 yearly frequency per event; (3) orig \u2013\
    \ boolean (True = historic WISC event; False = probabilistically perturbed); (4)\
    \ intensity \u2013 matrix of maximum wind gust speed per event (axis 0) and grid\
    \ cell (axis 1), units m/s. Grid coordinates provided in centroids/lat and centroids/lon\
    \ groups. Source: WISC historic footprints extended probabilistically; see README\
    \ for methods and references."
  download_url: https://www.research-collection.ethz.ch/entities/researchdata/7ebb4773-6413-4114-b96f-fba7e7e95dfe
  format: website
  id: WISC_prob_XXX
  spatial_resolution: 4400
  title: "Probabilistic Windstorm Hazard Event Set \u2013 XXX"
risk_data_type:
- hazard
schema: rdl-02
slug: rdls_hzd-jrc_drmkc_windstorm
spatial:
  countries:
  - AUT
  - BEL
  - BGR
  - HRV
  - CYP
  - CZE
  - DNK
  - EST
  - FIN
  - FRA
  - DEU
  - GRC
  - HUN
  - IRL
  - ITA
  - LVA
  - LTU
  - LUX
  - MLT
  - NLD
  - POL
  - PRT
  - ROU
  - SVK
  - SVN
  - ESP
  - SWE
  gazetteer_entries:
  - description: Europe
    id: Location_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6255148/europe.html
  scale: regional
title: Probabilistic Windstorm Hazard Event Set for Europe
version: '1'
vulnerability: null
---
